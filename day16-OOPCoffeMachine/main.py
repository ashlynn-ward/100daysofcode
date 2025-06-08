#OOP Coffee Machine
#Ashlynn Ward, May 16, 2025
#This program replicates the workings of a vending-machine-style coffee maker using object-oriented programming. 
#It can make 3 types of coffee, asks the user how many coins have been inserted, and 
#checks whether it has the right resources. It works the same as day15-CoffeeMachine.py

#Import classes that will be used
#Menu items are already defined within the Menu class
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Define objects for each of the 3 classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

#Store the coffee options using get_items method in Menu class
options = menu.get_items()

#When user enters "off" as their order, the program should stop
order = ""
while order!="off":
    #Prompt user for their order
    order = input(f"What would you like? {options}: ")
    #Validate input
    while order!="off" and order!="espresso" and order!="latte" and order!="cappuccino" and order!="report":
        order = input(f"Invalid input. What would you like? {options}: ")
    
    #If user chooses report, print resources
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    #If user chooses off, end program
    elif order == "off":
        break
    #Otherwise, make the user's chosen coffee
    else:
        drink = menu.find_drink(order)
        #Check if there are enough resources
        if coffee_maker.is_resource_sufficient(drink):
            #Print cost of drink
            print(f"Cost of {order} = {drink.cost}")
            #If payment goes through, make the drink
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

#Once program ends, print goodbye message
print("Turing off. Thank you for using the Coffee Machine!")