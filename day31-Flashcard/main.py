#Flashcards
#Ashlynn Ward, June 10, 2025
#This program uses a GUI to show users French flashcards. They can determine whether they know the word or not.
#After 3 seconds, the card automatically flips.

#Import os library
import os
#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Define constants
GREEN = "#B1DDC6"
FONT = "Ariel"

#Import tkinter, random, and pandas libraries
from tkinter import *
import random
import pandas

current_card = {}
to_learn = {}

#Access french and english words to learn and convert them to a dictionary
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_english_flashcard_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")

#Next card function randomly chooses a french word to show on the card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    current_card["French"]
    flashcard.itemconfig(language_text, text = "French", fill = "black")
    flashcard.itemconfig(word_text, text = current_card["French"], fill = "black")
    flashcard.itemconfig(card_background, image = card_front_img)
    #After 3 seconds, flip the card to the English side
    flip_timer = window.after(3000, flip_card)

#Is known function removes known words from the flashcard list
def is_known():
    global current_card
    flip_card()
    to_learn.remove(current_card)
    #Save list of words to learn
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index = False)
    #Call next card
    window.after(1000, next_card)

#Function flip card changes the info on the card to english
def flip_card():
    global current_card
    flashcard.itemconfig(card_background, image = card_back_img)
    flashcard.itemconfig(language_text, text = "English", fill = "white")
    flashcard.itemconfig(word_text, text = current_card["English"], fill = "white")
    window.after(1000, next_card)


#Create GUI
window = Tk()
window.config(bg = GREEN, padx = 50, pady = 50)
window.title("Flashcards")
flip_timer = window.after(3000, flip_card)
#Use canvas to create flashcard
card_front_img = PhotoImage(file = "card_front.png")
card_back_img = PhotoImage(file = "card_back.png")
flashcard = Canvas(width = 800, height = 526)
flashcard.config(bg = GREEN, highlightthickness = 0)
card_background = flashcard.create_image(400, 263, image = card_front_img)
language_text = flashcard.create_text(400, 150, text = "", font = (FONT, 40, "italic"))
word_text = flashcard.create_text(400, 263, text = "", font = (FONT, 60, "bold"))
flashcard.grid(row = 0, column = 0, columnspan = 2)
#Create buttons 
wrong_img = PhotoImage(file = "wrong.png")
wrong_button = Button(image = wrong_img, highlightthickness = 0, bd = 0, command = flip_card)
wrong_button.grid(row = 1, column = 0)
right_img = PhotoImage(file = "right.png")
right_button = Button(image = right_img, highlightthickness = 0, bd = 0, command = is_known)
right_button.grid(row = 1, column = 1)

#Call next card function to show the first flashcard
next_card()

#Keep window open
window.mainloop()