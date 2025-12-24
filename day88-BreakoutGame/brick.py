#Define the Brick class and allow it to inherit from Turtle
from turtle import Turtle

#Constant size of each brick
WIDTH = 88
HEIGHT = 12

class Brick(Turtle):
    def __init__(self, coordinate, colour):
        super().__init__()
        numBricks = 64
        self.shape("square")
        self.color(colour)
        self.shapesize(stretch_wid = 0.6, stretch_len = 4.4)
        self.penup()
        self.goto(coordinate)
        #Set bricks to visible - this will change as they are "destroyed"
        self.is_visible = True
        #Define location of brick to aid with collision detection
        self.half_width = WIDTH/2
        self.half_height = HEIGHT/2
        self.left = self.xcor() - self.half_width
        self.right = self.xcor() + self.half_width
        self.top = self.ycor() + self.half_height
        self.bottom = self.ycor() - self.half_height

    #Method destroy sets a block to invisible - occurs when it has been hit by ball
    def destroy(self):
        self.is_visible = False
        numBricks-=1
