#Upgraded Blog
#Ashlynn Ward, July 9, 2025
#This program is an upgraded version of Day 57's blog. It uses Bootstrap templates for design. 
#Note - one option to upgrade the form would be to send an email to the owner of the website. I did not add this feature. 

#Import modules
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#Request blog posts
posts = requests.get("https://api.npoint.io/3a7a5be41deb7154bddc").json()

message_sent=False

#Open pages 
@app.route("/")
def home_page():
    return render_template("index.html", posts = posts)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact", methods = ["GET", "POST"])
def contact_page():
    if request.method=="POST":
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        message=request.form['message']
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent=False)

@app.route("/post/<int:index>")
def post_page(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

#Run app
if __name__ == "__main__":
    app.run()