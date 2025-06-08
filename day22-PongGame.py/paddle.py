#Define the Paddle class and allow it to inherit from Turtle
from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 1, stretch_len = 5)
        self.penup()
        self.setheading(90)
        self.goto(coordinate)

    #Methods up  and down will move the paddle when the correct key is hit
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
