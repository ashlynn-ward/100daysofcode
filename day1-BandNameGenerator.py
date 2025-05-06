#Band Name Generator
#Ashlynn Ward, April 28, 2025
#This program prompts the user for some personal information and uses that to suggest a band name

#Print greeting
print("Welcome to the Band Name Generator!")
#Prompt and store user input
city_name = input("What's the name of the city you grew up in?")
pet_name = input("What's your pet's name?")
#Suggest band name using string concatenation
print("Your band name could be " + city_name + " " + pet_name)