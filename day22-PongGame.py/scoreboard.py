#Set alignment and font to constants
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

#Define Scoreboard class and inherit Turtle to it
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
    
    #l_point method adds a point to the left side and updates score
    def l_point(self):
        self.l_score+=1
        self.update()

    #r_point method adds a point to the right side and updates score
    def r_point(self):
        self.r_score+=1
        self.update()

    #update method clears the screen and rewrites the score
    def update(self):
        self.clear()
        self.goto(-40, 200)
        self.write(self.l_score, align = ALIGNMENT, font = FONT)
        self.goto(40, 200)
        self.write(self.r_score, align = ALIGNMENT, font = FONT)
