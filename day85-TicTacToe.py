#Tic Tac Toe
#Ashlynn Ward, September 12, 2025
#This program allows 2 users to play tic tac toe. It uses a matrix to store and compare values in the game.

#Welcome user
print("Welcome to Tic Tac Toe! Play against each other to get 3 in a row first.")

#Run program until users choose to stop game
run_program = "yes"
player = 1
while(run_program == "yes"):
    game_continue = True
    #Initialize gameboard matrix
    gameboard = [["E", "E", "E"], ["E", "E", "E"], ["E", "E", "E"]]
    
    for row in gameboard:
        print(row)

    #Begin round
    while(game_continue):

        #Declare which player's turn and prompt them to enter a location
        print(f"Player {player}, where would you like to play?")
        row = int(input("Row (1, 2, or 3): "))
        while(row!=1 and row!=2 and row!=3):
            row = int(input("Invalid input. Row (1, 2, or 3): "))
        col = int(input("Column (1, 2, or 3): "))
        while(col!=1 and col!=2 and col!=3):
            col = int(input("Invalid input. Column (1, 2, or 3): "))

        #Ensure player chooses a spot that hasn't already been chosen
        while (gameboard[row-1][col-1] != "E"):
            print(f"Player {player}, you chose a full spot. Where would you like to play?")
            row = int(input("Row (1, 2, or 3): "))
            col = int(input("Column (1, 2, or 3): "))

        #Change value on the gameboard
        if (player == 1):
            gameboard[row-1][col-1] = "X"
        else:
            gameboard[row-1][col-1] = "O"
        
        #Print gameboard
        for row in gameboard:
            print(row)

        #Check if player has won
        if (gameboard[0][0]==gameboard[0][1]==gameboard[0][2]!="E"):
            print(f"Player {player} wins!")
            game_continue = False
            run_program = input("Would you like to play again? Enter 'yes' or 'no': ")
        elif(gameboard[1][0]==gameboard[1][1]==gameboard[1][2]!="E"):
            print(f"Player {player} wins!")
            game_continue = False
            run_program = input("Would you like to play again? Enter 'yes' or 'no': ")
        elif(gameboard[2][0]==gameboard[2][1]==gameboard[2][2]!="E"):
            print(f"Player {player} wins!")
            game_continue = False
            run_program = input("Would you like to play again? Enter 'yes' or 'no': ")
        elif(gameboard[0][0]==gameboard[1][0]==gameboard[2][0]!="E"):
            print(f"Player {player} wins!")
            game_continue = False
            run_program = input("Would you like to play again? Enter 'yes' or 'no': ")
        elif(gameboard[0][1]==gameboard[1][1]==gameboard[2][1]!="E"):
            print(f"Player {player} wins!")
            game_continue = False
            run_program = input("Would you like to play again? Enter 'yes' or 'no': ")
        elif(gameboard[0][2]==gameboard[1][2]==gameboard[2][2]!="E"):
            print(f"Player {player} wins!")
            game_continue = False
            run_program = input("Would you like to play again? Enter 'yes' or 'no': ")
        elif(gameboard[0][0]==gameboard[1][1]==gameboard[2][2]!="E"):
            print(f"Player {player} wins!")
            game_continue = False
            run_program = input("Would you like to play again? Enter 'yes' or 'no': ")
        #If no one has won, change which player has a turn
        else:
            if(player == 1):
                player = 2
            else:
                player = 1
        #Error checking for run_program
        while(run_program!="yes" and run_program!="no"):
            run_program = input("Invalid input. Enter 'yes' or 'no': ")
#Print goodbye
print("Thanks for playing! Have a good day.")