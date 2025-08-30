#Age Guesser
#Ashlynn Ward, July 6, 2025
#This program prompts the user to enter their name. Then, it calls on the Agify and Genderize APIs to guess the user's age and gender.

#Import modules
from flask import Flask, render_template
import requests

app = Flask(__name__)

#Fill home screen
@app.route("/")
def hello():
    return "Hello! Enter /guess/name in the URL."

#Extract name and call on APIs
@app.route("/guess/<name>")
def guess(name):
    #Access gender
    gender_response = requests.get(url = f"https://api.genderize.io?name={name}")
    gender_response.raise_for_status()
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    #Access age
    age_response = requests.get(url = f"https://api.agify.io?name={name}")
    age_response.raise_for_status()
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, age = age, gender = gender)

#Run app
if __name__ == "__main__":
    app.run()