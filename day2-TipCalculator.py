#Tip Calculator
#Ashlynn Ward, April 29, 2025
#This program prompts the user for the bill, the size of tip, and the number of people dining, 
#then calculates how much each person should pay

#Print greeting
print("Welcome to the Tip Calculator!")

#Prompt and store user input for bill, tip, and number of guests
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? Suggested amounts: 10%, 12%, or 15% "))
guests = int(input("How many people to split the bill? "))

#Calculate total amount each person should pay
costPerPerson = (bill+bill*(tip/100))/guests
costPerPerson = round(costPerPerson, 2)

#Print results
print(f"Each person should pay: ${costPerPerson}")