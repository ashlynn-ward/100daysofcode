#Snake Game
#Ashlynn Ward, May 28, 2025
#This program is the snake game. The goal is to "eat" as much food as possible without running into the walls
#or the snake's own tail. The movement of the snake is controlled by the keyboard, and the snake continually
#grows in length

#Import screen, snake, food, and scoreboard classes
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
#Import time module
import time
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Create a Screen object
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
#Turn of screen tracer - the screen will not refresh until update is called
screen.tracer(0)

#Create snake
snake = Snake()
#Create food
food = Food()
#Create scoreboard
scoreboard = Scoreboard()

#Turn on event listeners for arrow keys to move snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Update screen
screen.update()

#Define a variable to keep track of whether game is running
game_is_on = True

#Begin game
while game_is_on:
    #Update screen
    screen.update()
    #Delay update by 1 second
    time.sleep(0.1)
    snake.move()
    #Detect collision with food, distance is 15 because the width of the food is 10 px, plus a buffer
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall, distance is 280 because snake head has a width of 20 px
    #If there is a collision, end game
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail, but skip the head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()

#Exit screen on click
screen.exitonclick()