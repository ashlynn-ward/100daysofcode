#Define constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE =  10
FINSIH_LINE_Y = 280

#Define player class and allow it to inherit Turtle
from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_player()
        self.setheading(90)

    #Move method moves the turtle up by the move distance
    def move(self):
        self.forward(MOVE_DISTANCE)

    #Reset player method moves the turtle back to its starting position
    def reset_player(self):
        self.goto(STARTING_POSITION)
