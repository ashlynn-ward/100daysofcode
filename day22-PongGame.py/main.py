#Pong Game
#Ashlynn Ward, May 30, 2025
#This program is the classic game Pong, where 2 players move paddles up and down to hit a ball

#Import time module
import time
#Import screen, paddle, ball, and scoreboard classes
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#Set up screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong")
#Turn off screen tracer to manually update screen
screen.tracer(0)

#Create paddles
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

#Create ball
ball = Ball()
screen.update()

#Create scoreboard
scoreboard = Scoreboard()

#Turn on event listeners
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

#Set a variable to determine whether game is on
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with the wall and bounce the ball
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce("wall")
    
    #Detection collision with right paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce("paddle")

    #Detect when the right paddle misses the ball
    if ball.xcor()>380:
        ball.reset_position()
        time.sleep(0.2)
        scoreboard.l_point()

    #Detect when the left paddle misses the ball
    if ball.xcor()<-380:
        ball.reset_position()
        time.sleep(0.3)
        scoreboard.r_point()
    
    #Limit the game so it eventually stops - once a player reaches a score of 5
    if scoreboard.l_score == 5:
        print("Left side won!")
        game_is_on = False
    elif scoreboard.r_score == 5:
        print("Right side won!")
        game_is_on = False
        
#Exit program when screen is clicked
screen.exitonclick()