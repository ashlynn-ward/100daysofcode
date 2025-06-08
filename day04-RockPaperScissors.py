#Rock, Paper, Scissors
#Ashlynn Ward, May 1, 2025
#This program is a rock, paper, scissors simulator. The program randomly chooses a move, 
#and the user enters their choice
#Note: to further develop this program, user choice could be validated, however, I have not yet learned 
#the syntax for loops, so I have not implemented it

#Import random module
import random

#Define rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Print greeting and store user input as an integer
user_choice = int(input("Welcome to Rock, Paper, Scissors! What is your choice? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
while user_choice!=0 and user_choice!=1 and user_choice!=2:
    user_choice = int(input("Invalid input. What is your choice? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))

#Randomly choice rock, paper, or scissors
computer_choice = random.randint(0,2)
#Print user and computer choice
if user_choice == 0:
    print(rock)
elif user_choice ==1:
    print(paper)
elif user_choice == 2:
    print(scissors)

print("Computer chose: ")
if computer_choice == 0:
    print(rock)
elif computer_choice ==1:
    print(paper)
else:
    print(scissors)

#Determine the winner
if user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 0 and computer_choice == 1:
    print("You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
