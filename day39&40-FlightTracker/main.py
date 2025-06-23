#Flight Tracker
#Ashlynn Ward, June 18, 2025
#This program requests flight prices from the Amadeus API to find the cheapest flights to predetermined cities. It then uses Sheety to update
#the flight info in a Google  Sheet, and sends the user an email notification.
#Note - before using, you must add your own API keys and emails into the code.

#Import datetime and timedelta modules and time library
from datetime import datetime, timedelta
import time

#Import FlightData, DataManager, FlightSearch and NotificationManager classes
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager

#Define origin airport
ORIGIN_CITY_IATA = "DTW"

#Create an object for each class
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()

#Get destination data
sheet_data = data_manager.get_destination_data()
print(sheet_data)

#If IATA code is missing in the Sheet, add it for each city and ubdate the destination data
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] == flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

#Access customer emails
customer_data = data_manager.get_customer_emails()
customer_email_list = [row["Email"] for row in customer_data]

#Search for flight prices
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting direct flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = flight_data.find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)
    #If no direct flights are found, check for indirect flights
    if cheapest_flight.price == "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flights...")
        stopover_flights = flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight = flight_data.find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price is: £{cheapest_flight.price}")

#Send an email if a chep flight is found
if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
    print(f"Lower price flight found to {destination['city']}!")
    if cheapest_flight.stops == 0:
        message = f"Low price alert! Only GBP {cheapest_flight.price} to fly direct "\
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                    f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
    else:
        message = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "\
                    f"with {cheapest_flight.stops} stop(s) "\
                    f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."  
    # Send emails to everyone on the list
    notification_manager.send_emails(email_list=customer_email_list, email_body=message)