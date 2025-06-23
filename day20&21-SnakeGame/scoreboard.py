#Import Turtle class
from turtle import Turtle

#Set constants for writing 
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

#Define Scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #Use highscore saved in data file
        try :
            with open("highscore.txt") as data:
                self.highscore = int(data.read())
        except ValueError:
            self.highscore = 0
        #The score will be displayed on the screen as a turtle object
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    #Define a method to write score on screen
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align = ALIGNMENT, font = FONT)

    #Define a method to increase the score
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

    #Reset method resets the game and shows the high score
    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
            #Update the highscore in the file
            with open("highscore.txt", mode = "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    #Define a method to print "game over" at the end of the game
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align = ALIGNMENT, font = FONT)