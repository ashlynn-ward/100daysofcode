#Calculator
#Ashlynn Ward, May 8, 2025
#This program is a standard calculator that computes addition, subtraction, multiplication, and division

#Define functions to complete calculations
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

#Define dictionary with operations and their corresponding functions
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

#Print greeting
print("Welcome to the Command Line Calculator!")

#Define a variable to check whether program should continue running
continue_running = "yes"
while continue_running == "yes":
    #Prompt user for both numbers and the operation
    num1 = float(input("What is the first number? "))

    #Define a variable to check whether answer should be the next num1
    keep_answer = "y"
    while keep_answer == "y":
        operator = input("+\n-\n*\n/\nPick an operation: ")
        num2 = float(input("What is the second number?"))
        #Determine what calculation to do based on the operation and print result
        answer = operations[operator](num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")
        #Ask user whether they would like to continue operations with the answer
        keep_answer = input(f"Type 'y' to continue calculations with {answer}. Type 'n' to start a new calculation: ")
        while keep_answer!="y" and keep_answer!="n":
            keep_answer = input(f"Invalid input. Type 'y' to continue calculations with {answer}. Type 'n' to start a new calculation: ")
        if keep_answer == "y":
            num1 = answer

    #Check whether user would like to continue running the program and validate answer
    continue_running = input("Would you like to do another calculation? Type 'yes' or 'no': ")
    while continue_running!="yes" and continue_running!="no":
        continue_running = input("Invalid input. Type 'yes' to do another calculation or 'no' to end program: ")

#Print goodbye message
print("Thanks for using the Command Line Calculator!")