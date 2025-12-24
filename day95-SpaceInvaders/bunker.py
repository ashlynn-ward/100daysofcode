#Define the bunker class and allow it to inherit from Turtle
from turtle import Turtle

class Bunker(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.height = 10
        self.width = 10
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid = 0.5, stretch_len = 0.5)
        self.penup()
        self.goto(x_cor, y_cor)