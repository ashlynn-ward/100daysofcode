#HTML Forms
#Ashlynn Ward, July 10, 2025
#The purpose of this program is to learn how to access data submitted in HTML forms using Flask.

#Import modules
from flask import Flask, render_template, request

app = Flask(__name__)

#Run home page
@app.route("/")
def home():
    return render_template("index.html")

#Access form data and display it
@app.route("/login", methods=["POST"])
def receive_data():
    username=request.form['name']
    password=request.form['password']
    return f"Name: {username}, Password:{password}"

#Run app
if __name__=="__main__":
    app.run()