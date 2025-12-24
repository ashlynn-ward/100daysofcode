#Breakout Game
#Ashlynn Ward, October 20, 2025
#This program uses OOP to create a replica of the Breakout Game. It uses turtle for a GUI. 

#Import time module
import time
from tkinter import messagebox
#Import screen, paddle, ball, and scoreboard classes
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick

#Set up screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Breakout")
#Turn off screen tracer to manually update screen
screen.tracer(0)

#Create paddle
paddle = Paddle((0, -250))

#CREATE BRICKS
bricks = []
def create_bricks():
    y_coor = 200
    colours = ["Red", "Orange", "Yellow", "Green", "Green", "Yellow", "Orange", "Red"]
    #Need 8 rows of bricks
    for i in range(0,8):
        row = []
        x_coor = -348
        #Need 8 bricks in each row
        for j in range(0,8):
            new_brick = Brick((x_coor, y_coor), colours[i])
            row.append(new_brick)
            new_brick.showturtle()
            x_coor+=98
        y_coor -=15
        bricks.append(row)

#Create bricks
create_bricks()

#Create ball 
ball = Ball()
screen.update()

#Create scoreboard
scoreboard = Scoreboard()

#Turn on event listeners
screen.listen()
screen.onkey(paddle.right, "Right")
screen.onkey(paddle.left, "Left")

#Set a variable to determine whether game is on
game_is_on = True
while game_is_on:
    #Call sleep to slow game play
    time.sleep(0.05)
    #Move the ball
    ball.move_ball()
    #DETECT COLLISION WITH BRICKS
    for row in bricks:
        index = -1
        i = 0
        for brick in row:
            if ball.brick_collision(brick):
                ball.bounce("brick")
                #Keep track of index of brick to remove
                index = i
                #hide that brick
                brick.clear()
                brick.hideturtle()
            i+=1
        #Remove any brick
        if index!=-1:
            row.pop(index)
    #DETECT COLLISION WITH PADDLE
    if ball.distance(paddle)<50:
        #Determine the collision angle with the paddle
        offset = ball.xcor()+paddle.xcor()
        ball.bounce("paddle", offset)
    if ball.wall_collision():
        ball.bounce("wall")
    #DETECT COLLISION WITH WALL AND END GAME - game_is_on = False
    if ball.ycor()<-280:
       game_is_on = False
    #DETECT BALL PAST A CERTAIN Y_VALUE 
    if ball.ycor()>280:
        #UPDATE SCOREBOAD AND RESET BRICKS/BALL
        bricks = []
        create_bricks()
        scoreboard.point()
        ball.reset_position()

    screen.update()
#Once loop has exited, show a message that game has ended and final score
messagebox.showinfo("Game Over", f"Your final score was {scoreboard.score}")
#Exit program when screen is clicked
screen.exitonclick()
