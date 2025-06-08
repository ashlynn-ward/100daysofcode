#Coffe Machine
#Ashlynn Ward, May 14, 2025
#This program replicates the workings of a vending-machine-style coffee maker. It can make 3 types of coffee,
#asks the user how many coins have been inserted, and checks whether it has the right resources.

#Create dictionary to store each type of coffee's info
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#Create dictionary to store inventory
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0
}

def check_resources(water, milk, coffee):
    """Function check_resources checks whether there are enough ingredients in resources to make the drink
    It returns which resource will run out"""
    if water>resources['water']:
        return "water"   
    if milk>resources['milk']:
        return "milk"  
    if coffee>resources['coffee']:
        return "coffee" 
    return "none"

def accept_coins(cost):
    """Function accept_coins prompts the user to enter how many of each coin they have and returns the amount paid"""
    quarters = int(input("How  many quarters? "))
    dimes = int(input("How  many dimes? "))
    nickels = int(input("How  many nickels? "))
    pennies = int(input("How  many pennies? "))
    return 0.25*quarters+0.1*dimes+0.05*nickels+0.01*pennies

#Create variable to store what the user wants the coffee machine to do
#Options will be the 3 types of coffee, to see a report of the resources, or to turn the machine off
option = "report"

#While user does not turn the machine off, continue to run the program
while option!="off":
    #Prompt user for their choice and validate input
    option = input("What would you like? (espresso/latte/cappuccino): ")
    while option!="off" and option!="espresso" and option!="latte" and option!="cappuccino" and option!="report" and option!= "refill":
        option = input("Invalid input. What would you like? (espresso/latte/cappuccino): ")
    #If user enter report, display the resources
    if option == "report":
        print(f"Water: {resources['water']} mL")
        print(f"Milk: {resources['milk']} mL")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${resources['money']}")
    #If off is entered, end the program
    elif option == "off":
        break
    #If refill is entered, allow the user to refill ingredients until they are done
    elif option == "refill":
        refill = ""
        while refill!="Done":
            refill = input("What would you like to refill (water/milk/coffee)? Type 'Done' when done.")
            #Validate input
            while refill!="water" and refill!="milk" and refill!="coffee" and refill!="Done":
                refill = input("Invalid input. What would you like to refill (water/milk/coffee)? Type 'Done' when done.")
            if refill != "Done":
                #Prompt user for how much they want to add
                amount = int(input(f"How much {refill} would you like to add?"))
                #Update ingredient
                resources[refill]+=amount

    #Otherwise, start the process of making the coffee
    else:
        #Check whether resources are available
        has_ingredients = check_resources(MENU[option]["ingredients"]['water'], MENU[option]["ingredients"]['milk'], MENU[option]["ingredients"]['coffee'])
        #If there are resources available, prompt user for money using the accept_coins function
        if has_ingredients == "none":
            print(f"Cost of {option} = {MENU[option]['cost']}")
            paid = accept_coins(MENU[option]["cost"])
            #If user did not enter enough money, print message to refund the money
            if paid<MENU[option]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            #If enough money was entered, update the resources, offer change, and print the drink made
            else:
                resources["money"]+=MENU[option]["cost"]
                resources["water"]-=MENU[option]["ingredients"]["water"]
                resources["milk"]-=MENU[option]["ingredients"]["milk"]
                resources["coffee"]-=MENU[option]["ingredients"]["coffee"]
                if paid>MENU[option]["cost"]:
                    print(f"Here is ${round(paid-MENU[option]['cost'], 2)} in change.")
                print(f"Here is your {option}. Enjoy!")

        else:
            print(f"Sorry, there is not enough {has_ingredients}.")
print("Turning off. Thank you for using the Coffee Machine!")
