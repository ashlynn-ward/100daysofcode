#US States Game
#Ashlynn Ward, June 3, 2025
#This program is a guessing game. The user is shown a blank map of the US, and they must enter as many states
#as they can. When a state is guessed, it is labelled on the map.

#Change directory to current working directory
import os
os.chdir(os.getcwd())

#Import turtle and pandas
import turtle
import pandas

#Set up screen
screen = turtle.Screen()
screen.title("US States Game")

#Add a map of the US to the screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#Create a list of guessed states
guessed_states = []

#While the user has not guessed all 50 states, prompt them to enter a new state
while len(guessed_states)!=50:
    #Prompt user to enter a state, and check whether guess is valid - casing does not matter
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "What's another state in the US?").title()
    data = pandas.read_csv("50_states.csv")
    all_states = data["state"].to_list()
    #If guess is valid, label the state on the map and add it to guessed states list
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        #Get coordinates from csv
        state_data = data[data["state"] == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item())
        t.write(answer_state)
    
    #If user enters exit, end game
    if answer_state == "Exit":
        #Store missing states using list comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        #Store all missing states as a csv
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
