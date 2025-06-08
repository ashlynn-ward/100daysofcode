#Turtle Race
#Ashlynn Ward, May 27, 2025
#This program asks the user to choose which turtle they think will win, then randomly moves 6 turtles 
#in a race to the right edge of the screen

#Import Turtle and Screen classes
from turtle import Turtle, Screen
#Import random module
import random

#Define a variable that checks whether the race has started 
is_race_on = False

#Create a screen and set its dimensions
screen = Screen()
screen.setup(width = 500, height = 400)

#Prompt user for their choice of the winner and validate input
user_guess = screen.textinput(title="Which turtle will win?", prompt = "Make your guess. Enter a colour: ")
while user_guess!="red" and user_guess!="orange" and user_guess!="yellow" and user_guess!="green" and user_guess!="blue" and user_guess!="purple":
    user_guess = screen.textinput(title="Invalid option.", prompt = "Which turtle will win? Enter a colour: ")

#Define a list of colours and an empty list to store the turtles
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

#Set the y-position for the first turtle
y_position = -70

#Create 6 instances of the turtle class
for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_position)
    y_position +=30
    all_turtles.append(new_turtle)

#Change is_race_on to begin the race
if user_guess:
    is_race_on = True

#Begin race
while is_race_on:
    for turtle in all_turtles:
        #If turtle has won, end the race and print the winner
        if turtle.xcor()>230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_guess:
                print(f"Congratulations, {user_guess} has won!")
            else:
                print(f"Sorry, {user_guess} lost; {winner} won.")
        #Otherwise, move turtle randomly
        else:
            rand_distance = random.randint(0,10)
            turtle.forward(rand_distance)


#Exit screen on click
screen.exitonclick()