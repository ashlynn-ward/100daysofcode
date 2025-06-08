#Turtle Etch-a-Sketch
#Ashlynn Ward, May 27. 2025
#This program uses the turtle graphics to simulate an Etch-a-Sketch on the screen. It uses event listeners
#to listen to keystrokes. 

#Import screen and turtle class
from turtle import Turtle, Screen

#Create objects of Turtle and Screen classes
tim = Turtle()
screen = Screen()

#Define functions to move tim because screen event listeners cannot take functions with arguments
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

#Define function to reset the screen and tim's position
def reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#Turn on listener
screen.listen()

#Use event listeners to make tim move
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "d", fun = turn_left)
screen.onkey(key = "a", fun = turn_right)
screen.onkey(key = "c", fun = reset)

#Keep screen up until it is clicked on
screen.exitonclick()