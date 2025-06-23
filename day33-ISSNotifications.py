#ISS Notifications
#Ashlynn Ward, June 12, 2025
#This program creates a pop-up on the screen when the ISS is above the user's latitude and longitude, and when the 
#sky is dark enough to see it (before sunrise or after sunset).

#Import tkinter, messagebox, datetime, and requests libraries
from tkinter import *
from tkinter import messagebox
import datetime as dt
import requests
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Save latitude and longitude (Currently set for Detroit)
USER_LONG = 42.331429
USER_LAT = -83.045753

#Function close to ISS returns true if the ISS's longitude and latitude are within 5 of the user
def close_to_iss():
    #Request latitude and longitude from ISS API and raise an error if error code is returned
    iss_response = requests.get(url = "http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    data = iss_response.json()
    #Save ISS longitude and latitude
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    #Determine whether user is within visible range of ISS
    if USER_LONG in range(int(iss_longitude)+5, int(iss_longitude)-5) and USER_LAT in range(int(iss_latitude)+5, int(iss_latitude)-5):
        return True
    else:
        return False

#Function is dark determines whether the time is before sunrise or after sunset
def is_dark(parameters):
    #Request data from sunset API and raise an error if an error code is returned
    sunset_response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    sunset_response.raise_for_status()
    data = sunset_response.json()
    #Save the hour of sunrise and sunset
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #Find current time
    current_time = dt.datetime.now()
    current_time = current_time.hour

    #Determine whether it is dark for user
    if current_time<=sunrise or current_time>=sunset:
        return True
    else:
        return False

#Create a dictionary to hold the parameters for API call to sunset
parameters = {
    "lat":USER_LAT,
    "lng":USER_LONG,
    "formatted":0,
}

#Call close_to_iss and is_dark functions to determine whether the ISS is visible to the user. If so, create a Tkinter popup
iss = close_to_iss()
dark = is_dark(parameters)

if iss and dark:
    window = Tk()
    notification = messagebox(title = "ISS Viewing", text = "The ISS is now visible in your area!")
