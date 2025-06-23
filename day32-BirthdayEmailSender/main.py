#Birthday Email Sender
#Ashlynn Ward, June 11, 2025
#This program automatically sends an email to whatever friends/family have a birthday on the current day.

#Import random, pandas, datetime, and smtp libraries
import random
import pandas
import datetime as dt
import smtplib

#Create empty letter and modified letter
letter = ""
modified_letter = ""

#Access today's date
today = (dt.datetime.now().month, dt.datetime.now().day)

#Open birthdays csv (Note: All information used is made up)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}
#Check if today matches with any of the birthdays
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    #If it is someone's birthday, pick a random letter and replace [NAME] with their name
    rand_num = random.randint(1,3)
    with open(f"letter{rand_num}.txt") as file:
        letter = file.read()
        modified_letter = letter.replace("[NAME]", birthday_person["name"])
    #Send the letter to the personal email address
    my_email = "test email"
    receive_email = birthday_person["email"]

    #Connect and log in to email securely
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user = my_email, password = "ENTER APP PASSWORD HERE")
    #Send message
    connection.sendmail(from_addrs = my_email, to_addrs = receive_email, msg = f"Subject:Happy Birthday!\n\n{modified_letter}")
    #Close connection
    connection.close()