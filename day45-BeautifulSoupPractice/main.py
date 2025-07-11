#Import BeautifulSoup class
from bs4 import BeautifulSoup

#Change working directory
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Open HTML file
with open("website.html") as file:
    contents = file.read()

#Create BeautifulSoup object
soup = BeautifulSoup(contents, "html.parser")
print(soup.title)

#Make a list of all paragraph items
all_p = soup.find_all(name = "p")

#Use selectors to access a single element
company_url = soup.select_one(selector = "p a")

#Scrape a live website - Note: this website is not live and was provided for this practice by the course
import requests
response = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
response.raise_for_status()
yc_website = response.text
soup2 = BeautifulSoup(yc_website, "html.parser")
#Find different sections
article_text = []
article_link = []
articles = soup2.find_all(name="a", class_="storylink")
for tag in articles:
    article_text.append(tag.getText())
    article_link.append(tag.get("href"))
article_upvote = soup2.find_all(name = "span", class_="score").getText()