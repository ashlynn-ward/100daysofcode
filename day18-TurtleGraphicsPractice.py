#Turtle Graphics Practice
#Ashlynn Ward, may 21, 2025
#This file contains code to learna nd practice using Turtle Graphics in python

#Import turtle class and random module
from turtle import Turtle, Screen
import random

#Create object
timmy = Turtle()
#Change timmy's attributes
timmy.shape("arrow")
timmy.color("blue")

#Draw a square
for i in range(0, 4):
    timmy.forward(100)
    timmy.left(90)

#Draw a dashed line
for i in range(0,7):
    timmy.forward(50)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()

#Define a function to randomly chooses a colour for the pen
def change_colour():
    r =random.randint(1,255)
    g =random.randint(1,255)
    b =random.randint(1,255)
    rand_colour = (r,g,b)
    return rand_colour

#Draw different shapes overlaid

#Define a function that takes number of sides to draw each shape in a random colour
def draw_shape(sides):
    for i in range(1,sides+1):
        #Colour of pen must be changed within Turtle class
        timmy.forward(100)
        timmy.left(360/sides)

#Draw shapes
for j in range(3, 11):
    timmy.pencolor(change_colour)
    draw_shape(j)

#Perform a random walk with different colors

#Define a list of directions
directions = [0, 90, 180, 270]
#Widen pen size and speed up turtle
timmy.width(15)
timmy.speed("fastest")
#Move the turtle a bunch of times, changing directions and colours randomly
for i in range(200):
    timmy.color(change_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

#Draw a spirograph

#Reset width
timmy.width(1)
#Define a function to draw overlapping circles in random colors until they stop overlapping
def draw_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        timmy.color(change_colour())
        timmy.circle(100)
        current_heading = timmy.heading() 
        timmy.setheading(current_heading+gap_size)

#Call the spirograph wiht a gap size of 5 degrees
draw_spirograph(5)

screen = Screen()
screen.exitonclick()

