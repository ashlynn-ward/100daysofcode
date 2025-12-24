#Text to Morse
#Ashlynn Ward, Seotember 9, 2025
#This program converts text input from the command line into morse code.

#Initialize dictionary with morse code
morse_code = {
    "A":"*-",
    "B":"-***",
    "C":"-*-*",
    "D":"-**",
    "E":"*",
    "F":"**-*",
    "G":"--*",
    "H":"****",
    "I":"**",
    "J":"*---",
    "K":"-*-",
    "L":"*-**",
    "M":"--",
    "N":"-*",
    "O":"---",
    "P":"*--*",
    "Q":"--*-",
    "R":"*-*",
    "S":"***",
    "T":"-",
    "U":"**-",
    "V":"***-",
    "W":"*--",
    "X":"-**-",
    "Y":"-*--",
    "Z":"--**",
    "1":"*----",
    "2":"**---",
    "3":"***--",
    "4":"****-",
    "5":"*****",
    "6":"-****",
    "7":"--***",
    "8":"---**",
    "9":"----*",
    "0":"-----",
    "?":"**--**",
    "!":"-*-*--",
    ".":"*-*-*-",
    ",":"--**--",
    ";":"-*-*-*",
    ":":"---***",
    "+":"*-*-*",
    "-":"-****-",
    "/":"-**-*",
    "=":"-**-",
}
#Initialize variable to store input
string = input("Enter the text you would like to convert: ")
#Convert string to all caps
string = string.upper()
#Change input to a list
string_list = list(string)
#For each item in the list, change the letter to morse code
morse = []
for char in string_list:
    #If char is a space, add space
    if char == " ":
        morse.append(" ")
    else:
        morse.append(morse_code[char])

#Print results
for char in morse:
    print(char, end = " ")