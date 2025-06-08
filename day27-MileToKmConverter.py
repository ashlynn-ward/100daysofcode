#Mile to Km Converter
#Ashlynn Ward, June 5, 2025
#This program uses tkinter to create a GUI miles to km converter. 

#Import tkinter library
from tkinter import *

#Function miles to km converts miles to km
def miles_to_km():
    miles = float(miles_input.get())
    km = miles*1.60934
    km = round(km)
    km_number.config(text = km)

#Create window
window = Tk()
window.minsize(400, 300)
window.title("Miles to km")

#Create labels and define their position using grid
miles_label = Label(text = "Miles")
miles_label.grid(row = 0, column = 2)
km_label = Label(text = "Km")
km_label.grid(row = 1, column = 2)
equal_label = Label(text = "is equal to")
equal_label.grid(row = 1, column = 0)
km_number = Label(text = "0")
km_number.grid(row = 1, column = 1)

#Create calculate button that calculates and updates the text of km number when button is pressed
calculate = Button(text = "Calculate", command = miles_to_km)
calculate.grid(row = 2, column = 1)

#Create entry box
miles_input = Entry()
miles_input.grid(row = 0, column = 1)



#Keep screen up while program is running
window.mainloop()