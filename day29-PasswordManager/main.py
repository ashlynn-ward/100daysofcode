#Password Manager
#Ashlynn Ward, Jun 7, 2025
#This program stores a user's passwords. It takes in the website and password, or it generates a random, secure
#password. 

#Import tkinter, json, random, and os libraries
from tkinter import *
from tkinter import messagebox
import json
import random
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Create password generator 
def generate_password():
    #Declare lists of accepted characters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #Define a list to store the password and fill it with a random number of random characters
    password_letters = [random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    random_password = password_letters + password_numbers + password_symbols

    #Shuffle the values in the list
    random.shuffle(random_password)

    #Join each character of the password
    "".join(random_password)

    #Set password to the input in password entry
    password_input.insert(0, random_password)

#Function save stores the password, username, and website in data.txt, then clears the entry boxes
def save():
    #Retrieve input
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }

    #If a field is empty, show an error pop up
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(title = "OOPS", message = "One or more fields were left empty. Please fill out all information.")
    #Otherwise, continue with save
    else:
        #Create a pop up message box
        message_output = messagebox.askokcancel(title = website, message = f"These are the details entered:\nUsername: {email}\nPassword: {password}\n Is it ok to save?")
        
        #If entry is ok, open or create file
        if message_output:
            try:
                with open("data.json", mode = "r") as file:
                    #Readthe data
                    data = json.load(file)
            except FileNotFoundError:
                #Create a new file and write to it if the file does not exist
                with open("data.json", mode = "w") as file:
                    json.dump(new_data, file, indent = 4)
            else:
                #Update the data
                data.update(new_data)
                with open("data.json", mode = "w") as file:
                    #Write info into file
                    json.dump(data, file, indent = 4)
            finally:
                #Clear entries
                website_input.delete(0,END)
                password_input.delete(0,END)

#Function find password looks through the saved passwords for the one matching the website entered, and returns the password in a pop up
def find_password():
    website_key = website_input.get()
    found_password = ""
    #Open password file
    try:
        with open("data.json") as file:
            data = json.load(file)
            found_password = data[website_key]
    #If no entries have been made, show a popup error
    except FileNotFoundError:
        messagebox.showerror(text = "You must enter a password before you can search.")
    #If website password does not exist, show a pop up error
    except KeyError:
        messagebox.showerror(text = f"There is no password saved for {website_key}.")
    #Show a popup with the password
    else:
        messagebox.showinfo(text = f"The password for {website_key} is {found_password}.")
            
#Set up UI
window = Tk()
window.minsize(240, 240)
window.title("Password Manager")
window.config(padx = 20, pady = 20)
#Add image as background using canvas
lock_img = PhotoImage(file ="logo.png")
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0, column = 1)
#Add labels
website_label = Label(text = "Website:")
website_label.grid(row = 1, column = 0)
email_label = Label(text = "Username/email:")
email_label.grid(row = 2, column = 0)
password_label = Label(text="Password:")
password_label.grid(row = 3, column = 0)
#Add entry boxes
website_input = Entry(width = 21)
website_input.grid(row = 1, column = 1)
website_input.focus()
email_input = Entry(width = 35)
email_input.grid(row = 2, column = 1, columnspan = 2)
#Populate email entry with the most commonly used email
email_input.insert(0, "example@email.com")
password_input = Entry(width = 21)
password_input.grid(row = 3, column = 1)
#Add buttons
#When password button is clicked, generate a random password and fill the password entry
password_button = Button(text = "Generate Password", command = generate_password)
password_button.grid(row = 3, column = 2)
#When add button is clicked, call save function
add_button = Button(text = "Add", width = 36, command = save)
add_button.grid(row = 4, column = 1, columnspan = 2)
#When search button is clicked, call find password function
search_button = Button(text = "Search", width = 13, command = find_password)
search_button.grid(row = 1, column = 2)

#Keep window open 
window.mainloop()