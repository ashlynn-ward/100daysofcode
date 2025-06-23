#Workout Tracker
#Ashlynn Ward, June 17, 2025
#This program uses a natural language API to extract info from user input. Then, it logs their daily workout in a Google Sheet.
#Note - you must add your own API key and ID for Nutritionix, as well as your own Sheety Endpoint to use

#Import os and datetime libraries, and requests module
import os
import datetime as dt
import requests

#Define constants
NUTRITIONIX_API_ID = os.environ.get("NUTRITION_API_ID")
NUTRITIONIX_API_KEY = os.environ.get("NUTRITION_API_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "ADD YOUR ENDPOINT HERE"

#Define header and parameters for Nutritionix
headers = {
    "x-app-id":NUTRITIONIX_API_ID,
    "x-app-key":NUTRITIONIX_API_KEY
}
#Prompt user to describe their workout
user_input = input("Tell me which exercises you did: ")
nutritionix_params = {
    "query":user_input
}

#Send a post request to Nutritionix API with the user input, and raise an error if an error code is returned
exercise_response = requests.post(url = NUTRITIONIX_ENDPOINT, json = nutritionix_params, headers = headers)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()

#Add the exercise data to the Google Sheet using Sheety API
today = dt.datetime.now()
day = today.strftime("%d/%m%/Y")
time = today.strftime("%H:%M:%S")
for exercise in exercise_data["exercises"]:
    sheet_params = {
        "workout":{
            "date":day,
            "time":time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url = SHEETY_ENDPOINT, json = sheet_params)
    sheet_response.raise_for_status()   