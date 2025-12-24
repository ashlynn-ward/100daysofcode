#Define the ball class and allow it to inherit from Turtle class
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = random.randint(-5,5)
        #Ensure that x_move is not 0
        while self.x_move == 0:
            self.x_move = random.randint(-5,5)
        self.y_move = 7
        self.move_speed = 1 #CHANGE SPEED
        self.radius = 10

    #Move method moves the ball to a new x and y coordinate
    def move_ball(self):
        new_x= self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto((new_x, new_y))

    #Bounce method determines what direction the ball should go after it hits a wall, paddle, or brick
    def bounce(self, side, offset=None):
            if(side == "wall"):
                self.x_move*=-1
            elif((side == "paddle" and self.xcor()>-250)or side == "brick"):
                 self.y_move*=-1
                 #Reset the ball's position so it doesn't get stuck in the paddle
                 if(side == "paddle" and offset is not None):
                     self.sety(-200)
                     #Set the x_move value based on the collision angle
                     max_x_speed = 2
                     self.x_move = offset*(max_x_speed/50)
                 

    #Reset position method sets ball to the original position
    def reset_position(self):
        self.move_speed = 0.1 #CHANGE SPEED
        self.goto(0,0)
    

    #FIX BRICK COLLISION
    #Method brick collision detects a collision with a brick
    def brick_collision(self, brick):
        #Find the distance from the ball to the brick based on the closest point to the brick
        closest_x = max(brick.left, min(self.xcor(), brick.right))
        closest_y = max(brick.bottom, min(self.ycor(), brick.top))
        distance_x = self.xcor() - closest_x
        distance_y = self.ycor() - closest_y
        distance_squared = (distance_x**2) + (distance_y**2)

        #If distance is smaller than the radius, the ball has collided
        hasCollided =  distance_squared < (self.radius**2)
        return hasCollided
    
    #Method wall collision determines if the ball has hit a wall
    def wall_collision(self):
        if(self.xcor()<-380 or self.xcor()>380):
            hasCollided = True
        else:
            hasCollided = False
        return hasCollided

