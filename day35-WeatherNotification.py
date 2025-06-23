#Weather Notification
#Ashlynn Ward, June 14, 2025
#This program calls an API to access the weather forecast, then sends the user an SMS message if it will rain.

#Import requests module, and smtp and os libraries
import requests
import smtplib
import os

#Define constants - longitude and latitude are for Detroit
USER_LAT = -83.046341
USER_LONG = 42.340115
SENDER_EMAIL = "test email"
RECEIVER_EMAIL = "test email"

#Access API key from environment variable
api_key = os.environ.get("OPEN_WEATHER_API_KEY")

#Define parameters for API
parameters = {
    "lat":USER_LAT,
    "lon":USER_LONG,
    "appid":api_key,
    "cnt":4
}

#Call Open Weather API to access weather data and raise an error if an error code is returned
response = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
#Open data as a JSON, and find the values for rain
will_rain = False
weather_data = response.json()
for i in range(0,4):
    code = weather_data["list"][i]["weather"][0]["id"]
    #Check whether it will rain - weather codes for rain in Open Weather mean it will rain
    if code<700:
        will_rain = True

#If it will rain, send user an email to bring an umbrella
if will_rain:
    #Connect and log in to email securely
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = SENDER_EMAIL, password = "ENTER APP PASSWORD HERE")
    #Send message
    connection.sendmail(from_addrs = SENDER_EMAIL, to_addrs = RECEIVER_EMAIL, msg = "Subject:Rainy day\n\nHello,\nIt's going to rain today. Better bring an umbrella ☔️.")
    #Close connection
    connection.close()