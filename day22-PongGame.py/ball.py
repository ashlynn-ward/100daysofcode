#Define the ball class and allow it to inherit from Turtle class
from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    #Move method moves the ball to a new x and y coordinate
    def move(self):
        new_x= self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto((new_x, new_y))

    #Bounce method determines what direction the ball should go after it hits a wall or paddle
    def bounce(self, side):
        if side == "wall":
            self.y_move*=-1
        elif side == "paddle":
            #Each time a paddle is hit, increase the speed
            self.x_move*=-1
            self.move_speed *=0.9

    #Reset position method sets ball to the original position
    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)
        self.bounce("paddle")

    #