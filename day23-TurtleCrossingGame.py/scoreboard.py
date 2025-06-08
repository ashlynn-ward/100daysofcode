#Define constants
FONT = ("Courier", 24, "normal")

#Define Scoreboard class and allow it to inherit Turtle class
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-230,260)
        self.update()
    
    #Update method changes the level and prints it
    def update(self):
        self.level+=1
        self.clear()
        self.write(f"Level: {self.level}", align = "center", font = FONT)

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER", align = "center", font = FONT)
