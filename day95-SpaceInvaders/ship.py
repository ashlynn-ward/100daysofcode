#Define the ship class and allow it to inherit from Turtle
from turtle import Turtle
from shot import Shot

class Ship(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.y_cor = -200
        self.move_speed = 20
        self.setheading(90)
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid = 2, stretch_len = 2)
        self.goto(x_cor, y_cor)
        self.can_shoot = True

    #begin method moves the ship to the playing position
    def begin(self):
        self.goto(0, -250)

    #move_right and move_left methods will move the ship
    def right(self):
        if(self.xcor()<350):
            new_x = self.xcor() + self.move_speed
            self.setx(new_x)

    def left(self):
        if(self.xcor()>-350):
            new_x = self.xcor() - self.move_speed
            self.setx(new_x)

    #fire method creates a shot and returns it to the main method
    def fire(self):
        new_shot = Shot(self.xcor(), self.ycor())
        return new_shot
    