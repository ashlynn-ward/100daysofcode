#Higher Lower Website
#Ashlynn Ward, July 4, 2025
#This program runs a classic higher lower game (like Day 14). However, it uses Flask to host it as a website. 

#Import modules
from flask import Flask
import random

app = Flask(__name__)

#Display guessing screen
@app.route("/")
def guess_number():
    return "<h1>Guess a number between 0 and 9</h1> <img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"

#Generate a random number
rand_num = random.randint(0,9)

#Parse URL and check if number is too high or too low. Print on screen
@app.route("/<int:guess>")
def check_number(guess):
    if int(guess) == rand_num:
        return "<h1 style=color:red>That's Right!</h1> <img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>"
    elif int(guess)>rand_num:
        return "<h1 style=color:purple>Too high</h1> <img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>"
    else:
        return "<h1 style=color:blue>Too low</h1> <img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>"

#Run server
if __name__ == "__main__":
    app.run()