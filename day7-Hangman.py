#Hangman 
#Ashlynn Ward, May 5, 2025
#This program is the game hangman. It chooses a random word, then prompts the user to guess it. 
#They have 6 lives, and if they guess incorrectly, they lose a life

#Import random module
import random

#Function print_guess prints the current guess
def print_guess():
    for i in range(0, len(current_guess)):
        print(current_guess[i], end = " ")
    print("\n")


#Define stages of the hangman and number of lives
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 5

#Define list of possible words
word_list = ["apple", "book", "desk", "pen", "cat", "dog", "tree", "house", "car", "phone",
             "computer", "laptop", "keyboard", "mouse", "chair", "table", "door", "window", "wall", "floor"]

#Generate a random word from the list above
answer = word_list[random.randint(0,19)]
print(answer)

#Define a list to keep track of guessed letters
guessed_letters = []

#Print greeting
print("Welcome to Hangman!")

#Create a list to store the state of the user's guess, and fill it with the right number of blank lines
current_guess = ["_"]
for num in range(1, len(answer)):
    current_guess.append("_")

#is_same is a boolean variable that will determine whether the user has guessed the word
is_same = False
#While user has not guessed the word and they have lives left, prompt user for letters
while not is_same and lives!=-1:
    #Print current guess
    print("Word to guess:", end=" ")
    print_guess()

    #Prompt user for a letter and convert it to lowercase
    guess = input("Guess a letter:")
    guess=guess.lower()
    
    #Check if letter has already been guessed
    already_guessed = 0
    for i in range(0, len(guessed_letters)):
        if guessed_letters[i] == guess:
            already_guessed +=1
    if already_guessed!=0:
        print("This letter has already been guessed.")
        continue
    else:
        guessed_letters.append(guess)


    #Update current guess and keep track of whether a letter was changed or not
    changed = 0
    for i in range(0, len(answer)):
        if answer[i]==guess:
            current_guess[i]=guess
            changed+=1

    #Print current guess
    print_guess()

    #If none of the letters were changed, remove 1 from lives
    if changed == 0:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives-=1
    
    #Print stage and number of lives
    print(stages[lives])
    print(f"****************************{lives+1}/6 LIVES LEFT****************************")

    #Check whether the current guess is the answer
    is_same = True
    for i in range(0, len(current_guess)):
        if current_guess[i]=="_":
            is_same = False

#Once game has ended, print a message that states whether the user won or lost
if lives ==-1:
    print("You ran out of lives. Game over.")
    print(f"Answer: {answer}")
else:
    print("You guessed the word. Congratulations!")