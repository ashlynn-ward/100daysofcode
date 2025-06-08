#Define constants
COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

#Import random module
import random

#Define car class and allow it to inherit turtle class
from turtle import Turtle
class Car(Turtle):
    def __init__(self, y_position):
        super().__init__()
        #Set colour to a random one from the colour list
        self.color(random.choice(COLOURS))
        self.shape("square")
        self.shapesize(stretch_wid = 1, stretch_len = 2)
        self.penup()
        self.goto(300, y_position)
        self.setheading(180)

    #Move cars method moves the cars by the move distance, which is affected by the level
    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(level-1))
    
