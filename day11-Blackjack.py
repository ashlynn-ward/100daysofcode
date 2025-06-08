#Blackjack
#Ashlynn Ward, May 9, 2025
#This program simulates the game Blackjack, where the user and computer are dealt cards, and whoever is 
#closest to 21 without going over wins

#Import random module
import random

#Define a list containing the possible cards drawn
#Note - this program does not consider the number of cards in a deck
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Define a dictionary that stores the number of each type of card left in the deck and fill it
deck = {}
for i in range(0, len(cards)):
    deck[cards[i]] = 4
cards_in_deck = 52

#Function calculate_score computes the score of a hand
def calculate_score(card, score):
    if card == "J" or card == "Q" or card == "K":
        score+=10
    #Only add 1 to score for aces here, determine whether or not to add the extra 10 in main program
    elif card == "A":
        score+=1
    else:
        score+=int(card)
    return score

#Define a variable to check whether program should continue or not and print greeting
keep_running = input("Welcome to Blackjack! Would you like to play a game? Type 'y' or 'n': ")
while keep_running!="y" and keep_running!="n":
    keep_running = input("Invalid input. Would you like to play a game? Type 'y' or 'n': ")
    
#Continue to runn game until user stops it
while keep_running == "y":
    #If half of the deck has been used, "reshuffle" it
    if cards_in_deck <=26:
        for i in range(0, len(cards)):
            deck[cards[i]] = 4
        cards_in_deck = 52

    #Define a variable to keep track of the number of A's in user's hand
    user_A = 0
    comp_A = 0

    #Choose 2 random cards for the user and the computer
    user_cards = []
    comp_cards = []
    user_score = 0
    comp_score = 0
    for i in range(0,2):
        user_cards.append(cards[random.randint(0,12)])
        comp_cards.append(cards[random.randint(0,12)])

        #If card chosen is no longer in deck, choose a new card
        while deck[user_cards[i]]==0:
            user_cards[i]= cards[random.randint(0,12)]
        #Remove the added cards fromt the deck
        deck[user_cards[i]]-=1
        while deck[comp_cards[i]]==0:
            comp_cards[i]= cards[random.randint(0,12)]
        deck[comp_cards[i]]-=1
        cards_in_deck -=2

        #Calculate user's and computer's score
        user_score = calculate_score(user_cards[i], user_score)
        #Determine whether ace should be equal to 11, or it should remain as the 1 that was already added
        if user_cards[i] == "A" and user_score<=10:
            user_score+=10
            user_A+=1
        comp_score = calculate_score(comp_cards[i], comp_score)
        if comp_cards[i] == "A" and comp_score<=10:
            comp_score+=10
            comp_A+=1
    
    #Print user's hand and computer's first card
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {comp_cards[0]}")

    #Ask user whether they would like another card if score is less than 21
    if user_score<21:
        new_card = input("Type 'y' to get another card, type 'n' to pass: ")
    else:
        new_card = "n"
    
    #Validate input
    while new_card!="y" and new_card!="n":
        new_card = input("Invalid input. Type 'y' to get another card, type 'n' to pass: ")
    
    #While user wants a new card, add a random card to their hand and print hands
    while new_card == "y":
        user_cards.append(cards[random.randint(0,12)])
        user_score = calculate_score(user_cards[len(user_cards)-1], user_score)
        #Determine whether aces should equal 11, or remain as the 1 that was added to score
        if user_cards[i] == "A" and user_score<=10:
            user_score+=10
            user_A+=1
        #If there is an ace present in the hand that is scored as 11, but it no longer should be, change its
        #value to 1
        while user_score>=21 and user_A>0:
            user_score -=10
            user_A-=1
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")
        if user_score<21:
            new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            new_card = "n"

    #While computer's score is less than 17, randomly add cards to its hand
    while comp_score<17:
        comp_cards.append(cards[random.randint(0,12)])
        comp_score = calculate_score(comp_cards[len(comp_cards)-1], comp_score)
        #Determine whether aces should equal 11, or remain as the 1 that was added to score
        if comp_cards[i] == "A" and comp_score<=10:
            comp_score+=10
            comp_A+=1
        #If there is an ace present in the hand that is scored as 11, but it no longer should be, change its
        #value to 1
        while comp_score>=21 and comp_A>0:
            comp_score -=10
            comp_A-=1
    
    #Print final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")

    #Determine winner and print results
    if user_score>21 and comp_score>21:
        print("Both hands went over. Push")
    elif user_score>21:
        print("Your hand went over. Oponent wins")
    elif comp_score>21:
        print("Oponent went over. You win!")
    elif comp_score == user_score:
        print("Scores are equal. Push")
    elif comp_score<user_score:
        print("Your hand is greater. You win!")
    else:
        print("Oponent's score is greater. Oponent wins") 
    
    #Ask user if they would like to play again, and validate input
    keep_running = input("\nWould you like to play again? Type 'y' or 'n': ")
    while keep_running!="y" and keep_running!="n":  
        keep_running = input("Invalid input. Would you like to play again? Type 'y' or 'n': ")

#Print goodbye message
print("Goodbye! Thank you for playing Blackjack!")