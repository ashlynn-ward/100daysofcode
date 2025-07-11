#Top 100 Movies
#Ashlynn Ward, June 24, 2025
#This program takes the top 100 movies from Web Archive's list, and save them to a list. Then, the user can delete the movies they have already seen.

#Define constants
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

#Import os library
import os
#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Import BeautifulSoup class and requests module
import requests
from bs4 import BeautifulSoup

#Access the website's data
response = requests.get(url = URL)
response.raise_for_status()
website_html = response.text

#Create BeautifulSoup object and access the movie titles
soup = BeautifulSoup(website_html, "html.parser")
all_movies = soup.find_all(name = "h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
#Reverse movie list
movie_titles.reverse()
with open("movie.txt", mode = "w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")
