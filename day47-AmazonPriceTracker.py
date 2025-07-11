#Amazon Price Tracker
#Ashlynn Ward, June 26, 2025
#This program scrapes Amazon for its price on a selected items. It then sends an email if the price drops. 

#Import libraries
from bs4 import BeautifulSoup
import requests
import smtplib

#Set target price
TARGET_PRICE = 100
PRODUCT = "Instapot"
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

#Define headers
headers = {
    "Accept_Language":"en-US",
    "User-Agent":"Enter User Agent",  
}

#Scrape Amazon 
response = requests.get(url = URL, headers = headers)
response.raise_for_status()
data = response.content
soup = BeautifulSoup(data, "html.parser")
#Pull out the prices
price = soup.find(class_ = "a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

#If price is lower than target, send an email
if price_as_float<TARGET_PRICE:
    #Connect and log in to email securely
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = "my_email", password = "ENTER APP PASSWORD HERE")
    #Send message
    message = f"The {PRODUCT} is now ${price_as_float}! \n Buy here: {URL}"
    connection.sendmail(from_addrs = "my_email", to_addrs = "receive_email", msg = f"Subject:Amazon Price Alert!\n\n{message}")
    #Close connection
    connection.close()