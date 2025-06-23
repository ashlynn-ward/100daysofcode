#Import smtp library
import smtplib

#This class is responsible for sending emails with the deal flight details
class NotificationManager:
    def __init__(self):
        self.my_email = "test email"
        self.receive_email = "test email"
    
    #Method send email sends an email with the flight info
    def send_emails(self, email_list, message):
        #Connect and log in to email securely
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user = self.my_email, password = "ENTER APP PASSWORD HERE")
        for user in email_list:
            #Send message
            connection.sendmail(from_addrs = self.my_email, to_addrs = user, msg = f"Subject:Low Flight Price\n\n{message}")
            #Close connection
        connection.close()