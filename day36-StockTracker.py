#Stock Tracker
#Ashlynn Ward, June 15, 2025
#This program tracks the daily stock prices of a company (currently set to Tesla), and sends a notification if they change by a certain percent.
#Note - this program does not currently do anything because test emails have been used. Also, dateshave been formatted for the API.
#However, it does not seem like the API is always up-to-date. Dates may have to be manually set to run.

#Import os, smtp, and datetime libraries, and request module
import os
import smtplib
from datetime import date, timedelta
import requests

#Define constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
SENDER_EMAIL = "test email"
RECEIVER_EMAIL = "test email"

#Save yesterday and the day before's dates in yyyy-mm-dd format
yesterday = date.today()-timedelta(days=1)
day = yesterday.day
if day<10:
    day = f"0{day}"
month = yesterday.month
if month<10:
    month = f"0{month}"
yesterday = f"{yesterday.year}-{month}-{day}"
day_before = date.today()-timedelta(days=2)
day = day_before.day
if day<10:
    day = f"0{day}"
month = day_before.month
if month<10:
    month = f"0{month}"
day_before = f"{day_before.year}-{month}-{day}"


#Define stock API parameters and news API parameters
stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "outputsize":"compact",
    "apikey":os.environ.get("ALPHA_VANTAGE_API_KEY")
}
news_parameters = {
    "q":COMPANY_NAME,
    "from":yesterday,
    "apiKey":os.environ.get("NEWS_API_KEY")
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#Access stock closing prices for the previous 2 days, and raise an error if an error code is returned
stock_response = requests.get(url = STOCK_ENDPOINT, params = stock_parameters)
stock_response.raise_for_status()

#Save the prices
stock_data = stock_response.json()
yesterday_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
day_before_price = float(stock_data["Time Series (Daily)"][day_before]["4. close"])

#Find absolute difference between the 2 days, then calculate the percentage difference
difference = abs(yesterday_price-day_before_price)
difference_percentage = (difference/((yesterday_price+day_before_price)/2))*100

#If difference_percentage is greater than 5, find 3 current articles related to the company and send them in an email
if difference_percentage>=5:
    news_response = requests.get(url = "https://newsapi.org/", params = news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    news_articles = []
    for i in range(0,3):
        news_articles.append(news_data["articles"][i]["title"])
    #Connect and log in to email securely
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = SENDER_EMAIL, password = "ENTER APP PASSWORD HERE")
    #Send message
    connection.sendmail(from_addrs = SENDER_EMAIL, to_addrs = RECEIVER_EMAIL, msg = f"Subject:{COMPANY_NAME} Stock Notification\n\n{COMPANY_NAME}'s Stock has changed by {difference_percentage}%./nArticles that may be related:\n- {news_articles[0]}\n- {news_articles[1]}\n- {news_articles[2]}\n")
    #Close connection
    connection.close()