#Password Generator
#Ashlynn Ward, May 2, 2025
#This program generates a random password based on criteria provided by the user

#Import random module
import random

#Print greeting
print("Welcome to the PyPassword Generator!")

#Declare lists of accepted characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Prompt user to enter password criteria
num_letters = int(input("How many letters would you like in your password?"))
num_symbols = int(input("How many symbols would you like?"))
num_num = int(input("How many numbers would you like?"))

#Define a list to store the password and randomly fill it
password = []
for num in range(0, num_letters):
    #Generate a random index and add that letter to the password
    index = random.randint(0, 51)
    password.append(letters[index])
for num in range(0, num_symbols):
    #Generate a random index and add that symbol to the password
    index = random.randint(0, 8)
    password.append(symbols[index])
for num in range(0, num_num):
    #Generate a random index and add that number to the password
    index = random.randint(0, 9)
    password.append(numbers[index])

#Shuffle the values in the list
random.shuffle(password)

#Print each character in the password, specify the end of each print to be an empty character
for character in password:
    print(character, end="")
