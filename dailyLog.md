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

Day 3 - April 30, 2025
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

 Day 15 - May 14, 2025
    Today, there wer no new topics covered. 2 things I learned while working on the project were that the round() function exists, which allows you to round a number to a certain number of decimal places, and that you should use single quotation marks when accessing dictionary values in f-strings.
    Project completed - Coffee Machine: this program acts as a vending machine-style coffee maker. It can 'make' 3 types of coffee. It also tracks how much of each resource is available and whether the user gives the correct amount of money. One thing that I would like to add to this program would be to allow the user to "restock" the machine.

Day 16 - May 15-16, 2025
    Topics covered - the basics of object-oriented programming.
        For day 16, I did an introduction to OOP. I learned what classes, objects, attributes, and methods are. I also learned how to create objects and access classes, attributes, and methods. I have not yet made my own classes. 
    Project completed - OOP Coffee Machine: this program is the same as day 15's Coffee Machine, except it implements OOP. I had no clue what I was doing when I began this project, but I quickly learned that creating objects for different classes is not just about storing attributes, but also having access to the methods. This helped a lot, and I feel good about my final code. I am still a bit unsure about OOP, so I definitely need more practice with it. All imported files were given to me to use through the Udemy course I am following.
    Note - I completed day 16 over 2 days. On May 15, it took me more than an hour to learn about OOP. I was feeling kind of overwhelmed by using it in a project, so I took a break, thought about how the code would work, and came back to it on May 16. I'm glad I did, because it took me another hour to finish the project.  

Day 17 - May 18, 2025
    Topics Covered - creqating attributes and methods
        Today's content cleared up a lot about OOP. On day 16, I felt that I was using code that I didn't understand, but now that I know how to create my own methods and attributes, OOP makes a lot more sense. 
    Project completed - Quiz Game: this program is a true/falsse quiz that includes 4 files. It has a list of questions that it transforms into objects, then asks the user each question. It also keeps track of the score. 
    Note - today, I had some extra time, so I returned to previous projects. I added input validation into day04-RockPaperScissors, I changed day11-Blackjack to simulate the number of each type of card in a deck, and I added an option to refill the ingredients in day15-CofffeeMachine. 

Note - I skipped May 19-25 to attend Google I/O 2025. 

Day 18 - May 26, 2025
    Topics Covered - Graphical User Interface and importing modules
        Today, I dug through Turtle Graphics documentation to complete several tasks with the turtle drawing module in Python (this practice can be found in day18-TurtleGraphicsPractice.py). I also learned different ways to import libraries and install packages from pypi. Lastly, I learned how to use the tuple data type to store rgb values.
    Project completed - Turtle Spot Painting: this program paints a picture that looks like the Spot Paintings by Damien Hirst. It required control of the turtle movements and pen, as well as extracting random colours using a library called colorgram.py. 
    Note - Today, I created my first virtual environment. I learned why venv's are important when using pip to install libraries, as well as how to activate/deactivate them, and how to install Python libraries.

Day 19 - May 27, 2025
    Topics covered - Object instances and states, higher order functions, and event listeners
        Everything I learned today was new, but it was pretty straightforward. It is interesting that when using event listeners, your code does not need to be running in some sort of loop until an input is given, but instead reacts to the user's input. Also, I learned that higher-order functions are common in python, but are not used in every programming language.
    Projects completed - Turtle Etch-a-Sketch: This program simulates the Etch-a-Sketch toy. It uses the w, a, s, and d keys to move and turn the turtle to draw pictures.
    Turtle Race: this program asks the user to choose a turtle that it think will win the race, then randomly moves 6 turtles until one has reached the end of the screen. This program relied on object instances, states, and randomization. 

Day 20 - May 28, 2025
    Topics covered - updating screens
        Today, I worked on a larger project, but one new thing that came up was turning off the screen tracer when using turtle so that I can control when the screen updates.
    Project - Snake Game: This program is the classic snake game, where a snake moves around the screen, controlled by the direction keys, and tries to eat as much food as it can without hitting its tail. This project will take 2 days to complete. Today, I created the snake using 3 connected turtles, I defined the snake in a class with several methods, and I figured out how to get it to move by itself and when the user presses a direction key. 

Day 21 - May 29, 2025
    Topics covered - class inheritance and slicing
        Today, I learned how to inherit methods and attributes into classes, and used inherited the Turtle class into my project. I also learned how to slice lists and tuples, and why that is useful.
    Project completed - Snake Game: I finished the snake game. I added the food to the screen, the score, and added collision detection with the food, walls, and the snake itself. 

Day 22 - May 30, 2025
    There were no new topics covered today. Instead, topics from the last few days (learning about turtle) were used in new ways. Today was the first day where I felt that I could write classes and call them confidently, and I did not ned to refer to course materials to get started on them.
    Project completed - Pong Game: this program is the classic game Pong. It uses turtle objects as paddles and a ball. When the ball hits the upper and lower walls, or the paddles, it bounces off in the other direction. If it hits one of the side walls, the opposing side gets a point. The ball continues to get faster, and the game ends when one player reaches a score of 5.

Day 23 - May 31, 2025
    There was no new content today Instead, I worked on a larger project
    Project completed - Turtle Crossing Game: this program is similar to hte game Crossy Road. The player moves the turtle using the up arrow while avoiding the oncoming cars. When the turtle reaches the top of the screen, a new level begins, and the car gets faster. This is the first project in turtle and OOP that I have completed entirely by myself. 

Day 24 - June 2, 205
    Topics covered - files, paths, and directories
        Today, I learned how to open, read, and write into external text files in Python. I also learned how to navigate paths.
    Project completed - Mail Merge: this program takes a written letter and a list of names, and personalizes each letter by replacing a placeholder with the correct name and saving it in a new file. 

Day 25 - June 3, 2025
    Topics covered - reading and writing csv files, and the pandas library
        Today, I learned what a csv file is. I was also introduced to the pandas library, which seems very useful for analyzing data. I have not yet read much of the documentation, but I did play aroudn with some methods in it, such as accessing different rows and columns, finding the max and mean of a column, and creating new csv files in a program.
    Project completed - US States Game: this program is a guessing game. A blank map of the US states is given, and the user must enter states they know. When a state is correctly inputted, it is labelled on the map. At the end, all of the states that the user did not get are saved in a csv file.
    Note - I am having trouble opening files in my programs (like text, csv, and images). Whenever I work on a project, I store the file at the same level as the main.py for easy access and to keep my workspace organized, but I keep getting errors that the file does not exit. I need to do more research about how to solve this problem.

Day 26 - June 4, 2025
    Topics covered - list and dictionarie comprehension
        Today, I learned how to create modified lists and dictionaries from existing lists/dictionaries using comprehension. This concept is going to reduce a lot of lines of code, and it is pretty simple to understand.
    Project completed - NATO Alphabet - this program prompts the user to enter a word, then prints the phonetic letters for the word. It uses dictionary comprehension to turn a dataframe into a dictionary, and it uses letter comprehension to turn the inputted word into the phonetic letters. 

Day 27 - June 5, 2025
    Topics covered - Tkinter, GUI, and Default, *args, and **kwargs
        Today, I was introduced to a new library: Tkinter. I built my first GUI without using turtle. I learned how to create a change widgets, different ways to set up their positions, and how to access input from the widgets. I also learned how to write functions that can take unlimited arguments.
    Project completed - Miles to Km Converter: this program prompts the user to enter a number of miles, then converts it to km. It users the tkinter library to create a GUI. 

Day 28 - June 6, 2025
    Topics covered - Canvas in Tkinter and Dynamic Typing
        Today, I learned how to overlay widgets in Tkinter using the canvas. I also learned how to use the after and after_cancel methods to wait a certain amount of time to refresh the screen and to cancel that functionality. This was useful for building a timer. Lastly, I looked at dynamic typing and how variables in Python can change data types throughout the program.
    Project completed - Pomodoro Timer: this program is a work timer. It uses Tkinter to create a GUI. When the start button is pressed, a 25-minute timer is started for work, followed by a 5-minute timer for a break. This is repeated 4 times. There is also a reset button that stops the timer. 