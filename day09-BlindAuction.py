#Blind Auction
#Ashlynn Ward, May 7, 2025
#This program stores bidder's names and bids in a dictionary. After each bidder, it clears the console
#so bidding is secret. At the end, the winner is revealed

#Import os system module
from os import system

#Define a variable to track the end of the program
continue_bidding = "yes"

#Define empty dictionary to store bidding info
bids = {}

#Program continues to run until user stops it
while continue_bidding == "yes":
    #Prompt user for bidding info
    current_bidder = input("What is your name?: ")
    bids[current_bidder] = input("What is your bid?: $")

    #Prompt user to either continue or end bidding
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    #While input is invalid, prompt user to enter 'yes' or 'no'
    while continue_bidding!="yes" and continue_bidding!="no":
        print("Invalid choice entered.")
        continue_bidding = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    #If user enters 'yes', clear console
    system("clear")

    #If user enters 'no', clear console and print results
    system("clear")

#Find highest bid and save the key
bidders = list(bids.keys())
max_bidder = bidders[0]
for index in bids:
    if bids[index]>bids[max_bidder]:
        max_bidder = index
    
#Print the highest bidder's info
print(f"The winner is {max_bidder} with a bid of ${bids[max_bidder]}.")
