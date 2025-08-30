#Blog Post
#Ashlynn Ward, July 6, 2025
#This program uses a Jinja template to create a blog posting site. Note - Gemini wrote the blog posts as filler text. The purpose
#of this project was to learn how to use Jinja.


#Import modules
from flask import Flask, render_template
import requests
from post import Post

#Access blog posts
posts = requests.get("https://api.npoint.io/3a7a5be41deb7154bddc").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["content"])
    post_objects.append(post_obj)

app = Flask(__name__)

#Show summary of each post on main page
@app.route('/')
def home():
    return render_template("index.html", posts=post_objects)

#When blog post is clicked, show all content
@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

#Run app
if __name__ == "__main__":
    app.run(debug=True)

