#Turtle Spot Painting
#Ashlynn Ward, May 26, 2025
#This program uses turtle graphics to "paint" a piece similar to Hirst's paintings.
#It paints randomly-colored dots on the screen

#Import Turtle class
from turtle import Turtle, Screen
#Import random module
import random

#Import Colorgram to extract colours from an uploaded Hirst painting
import colorgram
colors = colorgram.extract("spot_painting.jpg", 20)

#Convery extracted colors into rgb values
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

#Create a Turtle Object
timmy = Turtle()
#Change turtle's speed, move its pen up, and remove turtle graphic
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

#Move turtle to starting position
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

#Draw dots
number_of_dots = 100 
for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(rgb_colors))
    timmy.forward(50)
    #Move turtle to beginning of the next line when 1 line is complete
    if dot_count%10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
    

#Set screen to exit on click
screen = Screen()
screen.exitonclick()