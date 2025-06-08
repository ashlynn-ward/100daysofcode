#Import Turtle class
from turtle import Turtle

#List the starting positions of the snake
START_POSITIONS = [(0,0), (-20,0), (-40,0)]
#Set move to a constant value
MOVE_DISTANCE = 20
#Set directions as constants
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

#Declare the Snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            #Create pieces of the snake
            self.add_segment(position)

    #Define a method to add a segment to the snake
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    #Define a method ot reset the snake
    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    #Define a method to extend the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        #Move each piece of the snake to the place of the piece before it
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        #Move head forward
        self.head.forward(MOVE_DISTANCE)

    #Define methods to change the heading of the snake, but do not allow the snake to turn around
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)