#Import SMTP library
import smtplib

#Define email to send from (Note: no real email addresses are used in this file)
my_email = "test email"
receive_email = "receiving email"

#Connect and log in to email securely
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user = my_email, password = "ENTER APP PASSWORD HERE")
#Send message
connection.sendmail(from_addrs = my_email, to_addrs = receive_email, msg = "Subject:Hello\n\nHello!")
#Close connection
connection.close()