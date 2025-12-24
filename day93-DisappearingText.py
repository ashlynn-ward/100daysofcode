#Disappearing Text
#Ashlynn Ward, December 10, 2025
#This app helps users facing writer's block. When the program begins, the user has 10 seconds to type
#their next key, or else everything they have typed disappears.

#Define constants and global variables
GREEN = "#abf7b1"
FONT = "Monaco"
RED = "#d1001f"
BLACK = "#010B13"
WHITE = "#FFFFFF"
timer_id = None
time_left = 10

#Import tkinter, random, and pandas libraries
from tkinter import *
import random
import pandas

#run function changes the visible button, begins the timer, and changes the textbox to editable
def run():
    #If button currently is start, begin app
    if(start_end_button.cget('text') == "Start Writing"):
        #Allow user to begin typing
        textbox.config(state = NORMAL)
        #Begin by emptying the textbox
        textbox.delete("1.0", END)
        start_end_button.config(text = "End")
        #Bind keys to the type function
        textbox.bind("<Key>", type)
        #Start timer
        timer()
    #If text is equal to end, then reset the app
    else:
        start_end_button.config(text = "Start Writing")
        #Disable the textbox
        textbox.config(state = DISABLED)
        #Unbind keys from the type function
        textbox.unbind("<Key>")
        #End the timer
        window.after_cancel(timer_id)

#time_up function deletes all text when the timer is up
def time_up():
    global time_left
    #Reset textbox and warnings
    warning_text.pack_forget()
    textbox.delete("1.0", END)
    #Cancel the old timer
    if timer_id:
        window.after_cancel(timer_id)  
    #Reset time counter
    time_left = 10.0
    #Restart timer
    timer()
    

#Timer begins a timer for the app
def timer():
    global timer_id
    global time_left
    #End timer if needed
    if time_left <=0.0:
        #Reset timer
        timer_id = None
        time_left = 10
        time_up()
        #End timer function
        return
    #Display warning message if there are only 3 seconds left
    elif time_left <=3:
        warning_text.pack(padx = 10, pady = 10)
    #Otherwise, set a 0.1 second timer and decrement time left
    time_left-=0.1
    timer_id = window.after(100, timer) 

#type function resets the timer each time a key is pressed
def type(event):
    global time_left
    global timer_id
    #Unpack warning text
    if warning_text.winfo_ismapped():
        warning_text.pack_forget()    
    #Reset time_left
    time_left = 10
    #Remove old timer and start a new one
    if timer_id:
        window.after_cancel(timer_id)
    timer()

#Create GUI
window = Tk()
window.config(bg = GREEN, padx = 50, pady = 50)
window.title("Disappearing Text")

#Title text for app
title_text = Label(window, text = "Disappearing Text", font = (FONT, 40))
title_text.config(bg = GREEN, fg = BLACK)
title_text.pack(padx = 10, pady = 10)

#Warning text 
warning_text = Label(window, text = "Only 3 seconds until the text disappears!", font = (FONT, 20))
warning_text.config(bg = GREEN, fg = RED)
warning_text.pack(padx = 10, pady = 10)
#Hide the warning text
warning_text.pack_forget()

#Textbox for user to type in
textbox = Text(window, width = 100, height = 20, state = DISABLED)
textbox.pack(padx = 10, pady = 10)
textbox.config(bg = WHITE, fg = BLACK)

#Start/end button
start_end_button = Button(window, text = "Start Writing", command = run, relief = FLAT, font = (FONT, 15), width = 20, height = 2)
start_end_button.pack(padx = 10, pady = 10)

#Keep window open
window.mainloop()