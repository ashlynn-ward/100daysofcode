#Personal Name Card
#Ashlynn Ward, July 5, 2025
#This project is an online name card. It renders an HTML file using Flask.

#Import modules
from flask import Flask, render_template
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

app = Flask(__name__)

#Display "Hello World" on screen
@app.route("/")
def hello():
    return render_template("nameCard.html")

#Run server
if __name__ == "__main__":
    app.run()