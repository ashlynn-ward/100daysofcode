#Number Guessing Game
#Ashlynn Ward, May 11, 2025
#This program is a number guessing game. The computer randomly chooses a number between 1 and 100, and
#The user must choose the right number in a set number of guesses

#Import random module
import random

#Print greeting
print("Welcome to the Number Guessing Game!")

#Continue running the program until the user ends it
keep_running = "y"
while keep_running == "y":
    #Randomly choose a number
    answer = random.randint(1,100)
    print("I'm thinking of a number between 1 and 100.")

    #Prompt user for difficulty level and validate input
    level = input("Choose a level. Type 'easy' or 'hard': ")
    while level!="easy" and level!="hard":
        level = input("Invalid input. Type 'easy' or 'hard': ")
    #Determine the number of guesses based on the difficulty level
    if level == "easy":
        lives = 10
    elif level == "hard":
        lives = 5
    
    guess = 0
    #While user has not guessed the number and they still have guesses, prompt them to guess the number
    while guess!=answer and lives!=0:
        print(f"You have {lives} attempts left to guess the number.")
        guess = int(input("Make a guess: "))
        #Give a hint if guess is wrong, or print congratulations
        if guess>answer:
            print("Too high, guess again.")
            lives -=1
        elif guess<answer:
            print("Too low, guess again.")
            lives-=1
        else:
            print("Congratulations! You guessed the correct number!")
    
    #If user runs out of guesses, tell them the correct answer
    if lives == 0:
        print(f"You ran out of lives. The correct number was {answer}.")
    
    #Ask user if they would like to play again
    keep_running = input("Would you like to play again? Type 'y' or 'n': ")
    #Validate input
    while keep_running!="y" and keep_running!="n":
        keep_running = input("Invalid input. Would you like to play again? Type 'y' or 'n': ")

#Print goodbye message
print("Thank you for playing the Number Guessing Game!")