# 100daysofcode

Day 1 - April 28, 2025
    Topics covered - printing messages, strings and concatenation, inputs, commenting, and variables
        Today's content was simple, but it was important to practice the syntax of Python
        Something interesting I learned was that strings are a primitive data type in Python, unlike C, so they are easy to work with
    Project completed - Band Name generator: user is prompted to answer some questions, and a name for their band is suggested
    Note - Today, I set up my first git repo, and I read some documentation on git. I haven't yet pushed my project (I need to figure out how to do this), but I understand how git works

Day 2 - April 29, 2025
    Topics covered - primitive data types in Python, type checking, type conversion, mathematical operations, and f-strings
        Again, the content today was a review, but it was useful to learn some of the small differences that Python has compared to C when using operations on integers and floats
        2 things that stood out were the type() function to determine the data type of a value and f-Strings, which allow you to concatenate values and strings without having to type cast
    Project competed - Tip Calculator: user enters the bill, the size of tip, and how many people the bill will be split amongst, and the price that each guest must pay is calculated then printed

Dat 3 - April 30, 2025
    Topics covered - conditional operators and logical operators
        Today, the concepts were a review, but I learned how important indentation is in Python. Unlike other programming languages I have used, like C and javascript, curly braces are not used, so indentation differentiates parts of the conditions. 
    Project completed - Treasure Island: this is a 'Choose Your Own Adventure" style game, where user input determines what happens in the story.

Day 4 - May 1, 2025
    Topics covered - randomization, creating and using modules, and lists
        Today, I learned about some of the predefined functions to use on lists, such as count, append, sort, and remove. It is good to know what functions already exist because when I am solving problems, I have an idea of what tools I can use. 
    Project completed - Rock, Paper, Scissors: this is a classic game of Rock, Paper, Scissors, where the user enters their choice, and the computer randomly picks one of the 3 options. Then, the winner is determined.  
        Note - I would have liked to have added input validation for the user's choice, however, I do not yet know the syntax for loops in Python, and when I tried to add it, the program wasn't working. Maybe I will add it once I have learned about loops.

Day 5 - May 2, 2025
    Topics covered - for loops with lists and ranges
        Although I already understood the conept behind for loops, today I learned how they work in Python. It is interesting that they are linekd to lists, whereas in other programming languages, loops are basewd on incremented variables. 2 other things I discovered were the shuffle function, which shuffles the items in a list, and how to specify the end character when using print().
    Project completed - Password Generator: this program asks the user how many letters, numbers, and symbols they would like in their password, then randomly generates and shuffles the characters to create a secure password. 

Day 6 - May 4, 2025
    Topics covered - while loops and functions
        Today, I learned the syntax of while loops and functions. One important thing to remember is that function prototypes are not used in Python, so they should be declared at the beginning of the program.
    Project completed - Reeborg's World Maze: Today, I finished the maze level of Reeborg's World (link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json). It used functions and loops so the robot would find its way through the maze. 
    Here is the solution used: 
    
        #Function to turn right
        def turn_right():
            turn_left()
            turn_left()
            turn_left()

        #Find the edge of the maze
        while front_is_clear():
            move()
            turn_left()

        #Trace the right wall to the end
        while at_goal()!=True:
            if right_is_clear():
                turn_right()
                move()
            elif front_is_clear():
                move()
            else:
                turn_left()

Day 7 - May 5, 2025
    Today, no new topics were covered, instead I worked on a larger project.
        There were some things that I learned though. First, I discovered that the continue function can be used in python to end an iteration of a loop. Second, I learned that although you cannot define variables without initializing them, you can define lists that are empty. Lastly, a small things that I noticed is that you cannot increment or decrement values using ++ or --
    Project completed - Hangman: this is a classic game of hangman. A random word is chosen from a prewritten list of words, and the user must guess letters in the word. If they guess a wrong letter, they lose a life, and after six lives, they lose the game.
    Note - Today, I learned how to stage, commit, and push files to github, and I added all of my projects so far to my repo!

Day 8 - May 6, 2025
    Topics covered - Functions with parameters
        Today's content was similar to day 6, but I used functions with parameters. One thing that is notable is the difference between Keyword Arguments and Positional Arguments. If you do not want to worry about the order in which arguments are passed to a function, you can label them by their parameter names. When keywords are not used, arguments are passed to the parameters in the order they are written.
    Project completed - Caesar Cipher: this program prompts the user for a message and a shift number, then encodes of decodes the message using the Caesar cipher. One thing that is different about this program than others is that it continues to run until the user tells the program to stop. 
    Note - be careful when defining lists/variables in functions and loops. In this program, I create the encrypted_text and decrypted_text within functions, so they are not global. However, I accidentally created them within loops, so every time the loop ran, the string would be cleared. This was a difficult bug to find. 

Day 9 - May 7, 2025
    Topics covered - dictionaries and nested data structures
        Today I learned about a brand new data structure: dictionaries. They remind me of lists of structures in C. I now know how to creat dictionaries, add key-value pairs, and access values by their keys. I also understand how to access values in nested dictionaries and lists.
        One other function I learned about was system("clear") in the system module. This allows the program to clear the console. 
    Project completed - Blind Auction: this program allows users to hold a blind auction of however many bidders they would like. Each bidder is asked to enter their name and bid, then the console is cleared so the next bidder cannot see their info. At the end, the winner is revealed. 

Day 10 - May 8, 2025
    Topics covered - functions with outputs and docstrings
        Today's content went well with day 8, and it was a review of how return statements work. There were 2 things I learned that are unrelated to functions. First, you can have a function as a value in a dictionary. This is very useful when user input determines which function will run. Second, you can use f-strings in the input function. Although I did not learn anything new about the main topic for today, it was a good review of some of the intricacies of the first 10 days of the challenge. 
    Project completed - Calculator: this program is a calculator that can compute addition, subtraction, multiplication, and division. Although it sounds simple, I used some more complex alogrithms in my solution. First, I stored functions in a dictionary rather than using if-elif statements to determine which operation to use. Second, I used nested loops for continuity. The user decides when they are done with calculations on a certain answer, and they also decide when the total program will finish.

Day 11 - May 9, 2025
    Today, I did not learn any new content. Instead, I worked on a larger project. 
        One notable thing I discovered today was that in a Python function, when you use a return statement without a value, it returns a NoneType variable. This variable type overrides the previous variable type of wherever you store the function output. 
    Project completed - Blackjack: this program simulates a Blackjack game. The user and computer are randomly dealt 2 cards, and the user's cards and one of the computer's cards are revealed. Then, the user chooses whether they want another card or not, with the intention of the cards adding to 21 but not over it. One of the difficulties I had with this project was the ace. In Blackjack, ace either equals 11 or 1, depending if 11 will send the player's score over 21. I initially had the mechanism of choosing whether or not to add 11 in the score function, but I realized that it is difficult to return more than one value in functions. Also, the value of aces may need to change in 2 places. 
    Note - one concept that I did not address in my program was the limited number of cards of each type in a deck. I have thought about how to solve this problem, but did not have time to implement it. If I have extra time, I will create a dictionary to store the number of each card in the deck, then change that number each time a card is assigned to a player. If the number of cards reaches zero, the program will randomly choose another value for the card.

Day 12 - May 11, 2025
    Topics covered - Local and global scope
        Today's content was a review. One thing that is notable is that Python does not have block scope. So, if you create a variable in an if/else statement or loop, it has global scope (unless it is also created in a funciton).
    Project completed - Number Guessing Game: this program is a game that randomly generates a number between 1 and 100. Then, the user must guess the number in either 5 or 10 guesses. For each wrong guess, they are told whether the guessed number was too high or too low. This program ends when the user no longer wants to play. 

Day 13 - May 12, 2025
    Topics covered - debugging
        Today, I learned several useful tips on how to debug. Some of them I already use, such as using print statements to check values and trying to reproduce the bug. I also learned how to use a debugger. Although I have used one before, no one has ever explained to me exactly how it works. Now, I understand how to use breakpoints, step over, step into, and step into my code. 
    There was no project to complete today. Instead, I was given 3 programs to debug. In all 3, there were typos, mistakes with indentation, and logical errors with the kewords 'and' and 'or'. 

Day 14 - May 13, 2025
    Today, no new topics were covered. Instead, I worked on a larger project. While programming, I dived depper into how to import your own files into other files. I read up on how files  must be imported differently depending on how they are related. 
    Project completed - Higher Lower Game: this program imports information about celebrities from a list in another file that I created. Then, it randomly chooses 2 celebrities to display. The user must decide which celebrity has more Instagram followers. If they get it right, their score increases, and option B becomes option A. Then, a new person is chosen for option B, and a new round begins. Once the user gets it wrong, the game ends, and they have the option to play again. 