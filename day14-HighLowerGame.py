#Higher Lower Game
#Ashlynn Ward, May 13, 2025
#This program gives the users 2 celebrities and their bios (info linked from HigherLowerData.py)
#Then, the user must guess which celebrity has more followers on Instagram. The game ends when the user
#Choose the wrong celebrity

#Import the game data and random module
from higher_lower_data import data
import random

#Define a variable that determines when the program will end
keep_running = "y"

while keep_running == "y":
    #Randomly choose a person from data to be option A
    rand_index = random.randint(0,len(data)-1)
    option_A ={
        'name':data[rand_index]["name"],
        'follower_count':data[rand_index]["follower_count"],
        'description':data[rand_index]["description"],
        'country':data[rand_index]["country"]
    }
    #Define variable to track score
    score = 0

    #Define a variable to track when the user gets the answer wrong, and continue showing different options
    #for user to choose between until they get an answer wrong
    right = True
    while right == True:
        #Randomly choose a person from data to be option B
        rand_index = random.randint(0,len(data)-1)
        option_B ={
            'name':data[rand_index]["name"],
            'follower_count':data[rand_index]["follower_count"],
            'description':data[rand_index]["description"],
            'country':data[rand_index]["country"]
        }

        #Determine whether A or B has more followers (the one with more followers is the correct answer)
        if option_A["follower_count"]>=option_B["follower_count"]:
            correct_answer = "A"
        else:
            correct_answer = "B"
        
        #Print A and B's values and prompt user to enter their choice
        print(f"Compare A: {option_A['name']}, {option_A['description']}, from {option_A['country']}")
        print(f"Against B: {option_B['name']}, {option_B['description']}, from {option_B['country']}")
        guess = input("Who has more followers? Choose 'A' or 'B': ")
        #Validate input
        while guess != "A" and guess!="B":
            guess = input("Invalid input. Who has more followers? Choose 'A' or 'B': ")

        #If user was correct, update score, set option A to the current option B, and restart loop
        if guess == correct_answer:
            score+=1
            print(f"\nCorrect! {option_A['name']} has {option_A['follower_count']} million followers, and {option_B['name']} has {option_B['follower_count']} million.")
            print(f"Your score is {score}\n")
            option_A["name"] = option_B["name"]
            option_A["follower_count"] = option_B["follower_count"]
            option_A["description"] = option_B["description"]
            option_A["country"] = option_B["country"]
        else:
            #If user was wrong, print the correct answer and end the loop
            right = False
            print(f"\nThats wrong. {option_A['name']} has {option_A['follower_count']} million followers, and {option_B['name']} has {option_B['follower_count']} million.")
            print(f"Your final score is {score}\n")

    #Ask user if they would like to play again
    keep_running = input("Would you like to play again? Enter 'y' or 'n': ")
    #Validate input
    while keep_running!="y" and keep_running!="n":
        keep_running = input("Invalid input. Would you like to play again? Enter 'y' or 'n': ")


#Print goodbye message
print("\nThank you for playing Higher Lower!")