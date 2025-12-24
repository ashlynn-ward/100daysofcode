#Define the shot class and allow it to inherit from Turtle
from turtle import Turtle

class Shot(Turtle):
    #To create a shot, the x and y coordinates of the calling object must be passed
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid = 0.5, stretch_len = 1)
        self.penup()
        self.color("white")
        self.move_speed = 20
        self.setheading(90)
        self.goto(x_cor, y_cor)

    #shoot method moves the shot in the direction based on the object shooting
    def shoot(self, object):
        if object == "ship":
            self.forward(self.move_speed)
        elif object == "alien":
            self.backward(self.move_speed)

    #collision method determine if the shot collided with an object
    def collision(self, object):
        if(self.distance(object)<20):
            return True