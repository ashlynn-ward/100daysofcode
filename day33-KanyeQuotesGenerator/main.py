#Kanye Quotes Generator
#Ashlynn Ward, June 12, 2025
#This program uses a GUI to display Kanye West quotes. It makes an API request to kanye.rest to access the quotes.

#Import tkinter and requests libraries
from tkinter import *
import requests
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

def get_quote():
    #Get the quote through an API
    response = requests.get(url = "https://api.kanye.rest")
    #If an error code is given, raise an error
    response.raise_for_status()
    data = response.json()
    #Display quote on the screen
    canvas.itemconfig(quote_text, text = data["quote"])


#Create GUI
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
#When Kanya button is pressed, call the get_quote function
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()