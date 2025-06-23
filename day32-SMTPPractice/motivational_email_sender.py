#Motivational Email Sender
#Ashlynn Ward, Jun 11, 2025
#This program sends a motivational email on Mondays.

#Import datetime, random, and smtp libraries
import datetime as dt
import random
import smtplib

#Access the current datetime
now = dt.datetime.now()
day = now.weekday

#If it is a Monday, send an email
if day == 0:
    #Define email to send from (Note: no real email addresses are used in this file)
    my_email = "test email"
    receive_email = "receiving email"

    #Connect and log in to email securely
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = my_email, password = "ENTER APP PASSWORD HERE")
    #Choose a random quote to send from quotes list
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        motivation = random.choice(all_quotes)
    connection.sendmail(from_addrs = my_email, to_addrs = receive_email, msg = f"Subject:Motivation for Monday\n\n{motivation}")
    #Close connection
    connection.close()