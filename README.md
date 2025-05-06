# 100daysofcode

Day 1 - April 28, 2025
    Topics covered - printing messages, strings and concatenation, inputs, commenting, and variables
        Today's content was simple, but it was important to practice the syntax of Python
        Something interesting I learned was that strings are a primitive data type in Python, unlike C, so they are easy to work with
    Project completed - Band Name generator: user is prompted to answer some questions, and a name for their band is suggested
    Side Note - Today, I set up my first git repo, and I read some documentation on git. I haven't yet pushed my project (I need to figure out how to do this), but I understand how git works

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