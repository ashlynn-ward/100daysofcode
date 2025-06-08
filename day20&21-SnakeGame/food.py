#Import the Turtle class
from turtle import Turtle

#Import random module
import random

#Define a class for food that inherits from Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        #Set attributes
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("yellow")
        self.speed("fastest")
        #Set food to a random position on the screen
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)
    

        