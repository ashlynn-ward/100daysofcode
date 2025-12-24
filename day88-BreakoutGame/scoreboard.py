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
        self.score = 0
        self.update()
    
    #Point method adds a point to the left side and updates score
    def point(self):
        self.score+=1
        self.update()

    #update method clears the screen and rewrites the score
    def update(self):
        self.clear() 
        self.goto(0, 200) #MAY NEED TO CHANGE LOCATION
        self.write(self.score, align = ALIGNMENT, font = FONT)
    