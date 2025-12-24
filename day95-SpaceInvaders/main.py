#Space Invaders
#Ashlynn Ward, December 15, 2025
#This program is a remake of the classic space invaders game. The user must shoot all the aliens before they get shot.

#Import libraries
from turtle import Screen
from ship import Ship
from alien import Alien
from shot import Shot
from bunker import Bunker
import time
import random
from tkinter import messagebox

#Set up screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Space Invaders")

#Turn off screen tracer to manually update screen
screen.tracer(0)

#Define score
score = 0

#Create bunkers
bunker0 = []
bunker1 = []
bunker2 = []
start_x = [-325, -75, 175]
for i in range(0,3):
    #Create all upper pieces of the bunker and add to the array
    x_cor = start_x[i]
    for j in range(0,15):
        y_cor = -150
        new_piece = Bunker(x_cor, y_cor)
        x_cor+=10
        if i == 0:
            bunker0.append(new_piece)
        elif i == 1:
            bunker1.append(new_piece)
        else:
            bunker2.append(new_piece)
    #Create all lower pieces and add to the array
    x_cor = start_x[i]
    for k in range(0,15):
        y_cor = -160
        new_piece = Bunker(x_cor, y_cor)
        x_cor+=10
        if i == 0:
            bunker0.append(new_piece)
        elif i == 1:
            bunker1.append(new_piece)
        else:
            bunker2.append(new_piece)

#create_aliens function creates a new fleet of aliens
aliens = []
def create_aliens():
    y_cor = 250
    for j in range(0,5):
        x_cor = -350
        for i in range(0,11):
            new_alien = Alien(x_cor, y_cor)
            aliens.append(new_alien)
            x_cor +=30
        y_cor -=30

#cannon function creates shots for the ship - called when space is pressed
ship_shots = []
alien_shots = []
def cannon():
    global ship_shots
    global ships
    global current_ship
    ship = ships[current_ship]
    #Only shoot if the cooldown time has passed
    if(ship.can_shoot):
        ship_shots.append(ship.fire())

#Create a fleet of 3 ships
ships = []
y_cor = -275
x_cor = -375
for i in range(0,3):
    new_ship = Ship(x_cor, y_cor)
    x_cor +=25
    ships.append(new_ship)

#Keep track of current ship being used
current_ship = 2
#Link arrow keys to current ship and set up first ship
ships[current_ship].begin()
screen.update()
screen.listen()
screen.onkey(ships[current_ship].right, "Right")
screen.onkey(ships[current_ship].left, "Left")
screen.onkey(cannon, "space")

#Set a max number of alien shots allowed at a given time
max_shots = 4

#Begin game
runtime = 0
direction = "right"
while len(ships)>0:
    #Slow down play time
    time.sleep(0.3)
    #Count how many times game loop runs - used to determine when to move aliens
    runtime+=1

    #Only allow user to shoot every other frame
    if(ships[current_ship].can_shoot):
        ships[current_ship].can_shoot = False
    else:
        ships[current_ship].can_shoot = True

    #If there are no aliens left on the screen, create a new fleet
    if(len(aliens) == 0):
        #Increase max shots
        max_shots +=3
        create_aliens()

    #Determine whether an alien will shoot
    if(Alien.lottery() == 1):
        #Only create a shot if there are less than 7 shots currently on the screen
        if(len(alien_shots)<max_shots):
            #Choose a random alien to shoot
            index = random.randint(0, len(aliens)-1)
            #Create the shot
            new_alien_shot = Shot(aliens[index].xcor(), aliens[index].ycor())
            alien_shots.append(new_alien_shot)

    #Move all the shots currently in the game
    for shot in ship_shots:
        shot.shoot("ship")
    for shot in alien_shots:
        shot.shoot("alien")

    #Move all aliens left or right
    if len(aliens)>0:
        x_coords = [alien.xcor() for alien in aliens]
        left = min(x_coords)
        right = max(x_coords)
        if(left<-350):
            direction = "right"
        elif(right>350):
            direction = "left"
        for alien in aliens:
            #Move aliens down every 10 seconds  
            if(runtime%33 == 0):
                alien.move("down")
            alien.move(direction)
    
    for shot in ship_shots[:]:
        #Remove all shots that are no longer on the screen
        if(shot.ycor()>300):
            ship_shots.remove(shot)
            continue
        #Detect collisions between the shots and aliens
        for alien in aliens[:]:
            if(shot.collision(alien)):
                #Increase score by 10 each time an alien is shot
                score+=10
                #Delete alien and shot
                alien.hideturtle()
                aliens.remove(alien)
                shot.hideturtle()
                ship_shots.remove(shot)
                break
        #Detect collisions between shots and bunkers
        if(shot.xcor()<-150 and shot.xcor()>-350):
            for piece in bunker0:
                if(shot.collision(piece)):
                #Delete shot and piece of bunker
                    piece.hideturtle()
                    bunker0.remove(piece)
                    shot.hideturtle()
                    ship_shots.remove(shot)
                    break
        elif(shot.xcor()>-100 and shot.xcor()<100):
            for piece in bunker1:
                if(shot.collision(piece)):
                #Delete shot and piece of bunker
                    piece.hideturtle()
                    bunker1.remove(piece)
                    shot.hideturtle()
                    ship_shots.remove(shot)
                    break
        elif(shot.xcor()>150 and shot.xcor()<350):
            for piece in bunker2:
                if(shot.collision(piece)):
                #Delete shot and piece of bunker
                    piece.hideturtle()
                    bunker2.remove(piece)
                    shot.hideturtle()
                    ship_shots.remove(shot)
                    break

    for shot in alien_shots[:]:
    #Remove all shots that are no longer on the screen
        if(shot.ycor()<-300):
            alien_shots.remove(shot)
            continue
    #Detect collisions between the shots and ship
        if(current_ship>=0):
            if(shot.collision(ships[current_ship])):
                #Delete shot and ship
                    broken_ship = ships[current_ship]
                    broken_ship.hideturtle()
                    ships.remove(broken_ship)
                    current_ship -=1
                    #If there are ships remaining, then start the next one
                    if(current_ship>=0):
                        ships[current_ship].begin()
                        screen.onkey(ships[current_ship].right, "Right")
                        screen.onkey(ships[current_ship].left, "Left")
                    shot.hideturtle()
                    alien_shots.remove(shot)
                    continue          
        #Detect collisions between shots and bunkers
        if(shot.xcor()<-150 and shot.xcor()>-350):
            for piece in bunker0:
                if(shot.collision(piece)):
            #Delete shot and piece of bunker
                    piece.hideturtle()
                    bunker0.remove(piece)
                    shot.hideturtle()
                    alien_shots.remove(shot)
                    break
        elif(shot.xcor()>-100 and shot.xcor()<100):
            for piece in bunker1:
                if(shot.collision(piece)):
                    #Delete shot and piece of bunker
                    piece.hideturtle()
                    bunker1.remove(piece) 
                    shot.hideturtle()
                    alien_shots.remove(shot)
                    break
        elif(shot.xcor()>150 and shot.xcor()<350):
            for piece in bunker2:
                if(shot.collision(piece)):
            #Delete shot and piece of bunker
                    piece.hideturtle()
                    bunker2.remove(piece)
                    shot.hideturtle()
                    alien_shots.remove(shot)
                    break
    screen.update()

#At the end of the game, display a pop up with the final score
messagebox.showinfo("Space Invaders", f"Game Over\nFinal Score: {score}")
#Exit program when screen is clicked
screen.exitonclick()