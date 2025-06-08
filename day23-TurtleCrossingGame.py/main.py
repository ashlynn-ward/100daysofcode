#Turtle Crossing Game
#Ashlynn Ward, May 31, 2025
#This porgram is similar to the game Crossy Road. The user controls a turtle that begins at the bottom of 
#the screen. The goal is to move the turtle to the other side without being hit by a car. Each level, the 
#cars get faster.

#Import the time  and random modules
import time
import random

#Import screen, player, car,gameOver, and scoreboard classes
from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard, GameOver

#Set up screen
screen = Screen()
screen.setup(width = 600, height = 600)
screen.title("Turtle Crossing")

#Create player and scoreboard
player = Player()
scoreboard = Scoreboard()
#Create an empty list to hold cars
cars = []

#Turn on event listener
screen.listen()
screen.onkey(player.move, "Up")

#Turn of tracer to control screen updates
screen.tracer(0)

#Define a variable to determine whether game is running
game_is_on = True
while game_is_on:
    #Update the screen every 0.1 seconds
    time.sleep(0.1)
    screen.update()

    #Randomly create cars at random y position
    create_car = random.randint(0,6)
    if create_car == 1:
        cars.append(Car(random.randint(-230,250)))
    
    #Move all cars 
    for car in cars:
        car.move(scoreboard.level)
    
    #Detect when the player reaches the finish line and reset the game
    if player.ycor()>280:
        player.reset_player()
        scoreboard.update()

    #Detect collision between turtle and car
    for car in cars:
        if player.distance(car)<20:
            game_over = GameOver()
            game_is_on = False

#Exit screen on click
screen.exitonclick()