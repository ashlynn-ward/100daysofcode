#Import requests and HTTPBasicAuth modules
import requests
from requests.auth import HTTPBasicAuth

#Define constants
SHEETY_ENDPOINT = "YOUR SHEETY ENDPOINT"

#Data Manager class is responsible for talking to the Google Sheet
class DataManager:
    def __init__(self):
        self._user = "SHEETY USERNAME"
        self._password = "SHEETY PASSWORD"
        # Save your Sheety endpoints an environment variables
        self.prices_endpoint = "SHEETY PRICES ENDPOINT"
        self.users_endpoint = "SHEETY USERS ENDPOINT"
        self._authorization = HTTPBasicAuth(self._user, self._password)
        # Destination and Customer fields data start out empty
        self.destination_data = {}
        self.customer_data = {}    

    #Method get destination data gets data from Sheety API, raises an error if an error code is returned, and returns the data
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    #Method update destination data calls put to update the data in the sheet
    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "prices": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            response.raise_for_status()

    #Method get customer emails accesses the emails inputted in the Google Form
    def get_customer_emails(self):
        response = requests.get(url=self.users_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data