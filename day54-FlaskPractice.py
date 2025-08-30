#Flask Practice
#Ashlynn Ward, July 3, 2025
#This file is used for Flask and function decorator practice. It is my first server. 

#Import modules
from flask import Flask

app = Flask(__name__)

#Render Hello World on Screen
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#If /bye is added to url, render Bye on screen
@app.route("/bye")
def bye():
    return "<p>Bye</p>"

#Run server
if __name__ == "__main__":
    app.run()
