#Define the alien class and allow it to inherit from Turtle
from turtle import Turtle
import random

class Alien(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color("green")
        self.penup()
        self.shape("circle")
        self.goto(x_cor, y_cor)
        self.move_speed = 10
    
    #move method moves the aliens left and right
    def move(self, direction):
        if(direction == "left"):
            new_x = self.xcor()-self.move_speed
            self.goto(new_x, self.ycor())
        elif(direction == "right"):
            new_x = self.xcor()+self.move_speed
            self.goto(new_x, self.ycor())
        elif(direction == "down"):
            new_y = self.ycor()-self.move_speed
            self.goto(self.xcor(), new_y)
    
    #lottery determines whether an alien will shoot or not
    @staticmethod
    def lottery():
        return random.randint(1,10)