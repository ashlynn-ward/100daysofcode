#Pomodoro Timer
#Ashlynn Ward, June 6, 2025
#This program is a productivity timer. It runs as a window in the background, changing between a 25 minute 
#work timer and a 5 minute break timer. Every time the timer ends, it appears as the prominent window
#so the user knows that their time is up.

#Define constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

#Keep track of reps and timer
reps = 0
my_timer = None

#Import tkinter and math libraries
from tkinter import *
import math
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Set up timer mechanism - function start timer calls the countdown
def start_timer():
    global reps
    reps+=1
    #Determine how long the timer should be for and change title
    if reps%2!=0:
        timer_label.config(text = "Work", fg = GREEN)
        countdown(WORK_MIN*60)
        #Set checkmark text to have the number of checkmarks as work sessions have completed
        checkmark_text = ""
        for i in range(0, math.floor(reps/2)):
            checkmark_text += "✔︎"
        checkmarks.config(text = checkmark_text)
    elif reps%2 == 0 and reps%8!=0:
        timer_label.config(text = "Break", fg = PINK)
        countdown(SHORT_BREAK_MIN*60)
    else:
        timer_label.config(text = "Break", fg = RED)
        countdown(LONG_BREAK_MIN*60)
    
#Reset function resets labels, checkmarks, and reps
def reset():
    global my_timer
    global reps
    window.after_cancel(my_timer)
    reps = 0
    timer_label.config(text = "Timer")
    checkmark_text = ""
    checkmarks.config(text = checkmark_text)
    canvas.itemconfig(timer_text, text = "00:00")


#Set up countdown mechanism - function countdown uses the method after to recursively countdown
def countdown(count):
    global my_timer
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds <10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count>0:
        my_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()

#Set up UI
window = Tk()
window.title("Pomodoro Timer")
window.config(padx = 100, pady = 50, bg = YELLOW)

#Use height and width of background image
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
#Add text for timer
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font =(FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

#Add timer label
timer_label = Label(text = "Timer", fg = GREEN, font = (FONT_NAME, 50), bg = YELLOW)
timer_label.grid(row = 0, column = 1)

#Add buttons
#Start countdown when start button is pressed
start_button = Button(text = "Start", highlightthickness = 0, command = start_timer, bg = YELLOW)
start_button.grid(row = 2, column = 0)
#Reset timer and labels when reset button is pressed
reset_button = Button(text = "Reset", highlightthickness = 0, command = reset, bg = YELLOW)
reset_button.grid(row = 2, column = 2)

#Add a label to show checkmarks for each timer done
checkmarks = Label(fg = GREEN, bg = YELLOW)
checkmarks.grid(row = 3, column = 1)



#Keep window open
window.mainloop()