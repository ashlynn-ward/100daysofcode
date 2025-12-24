#Define the Paddle class and allow it to inherit from Turtle
from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid = 1, stretch_len = 5)
        self.penup()
        self.setheading(0) #CHANGE POSITION
        self.goto(coordinate)
        self.move_speed = 30

    #Methods right and left will move the paddle when the correct key is hit
    def right(self):
        new_x = self.xcor() + self.move_speed
        self.setx(new_x)
    def left(self):
        new_x = self.xcor() - self.move_speed
        self.setx(new_x)
