#Mail Merge
#Ashlynn Ward, June 2, 2025
#This program replaces and prints the same letter to different people by reading the letter and a list of 
#names from other files

#Import change_directory library and change working directory so program can access files
import os
import sys

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Set constants
PLACEHOLDER = "[name]"

#Read names file
with open("names.txt") as names_file:
    names = names_file.readlines()

#Read the letter
with open("starting_letter.docx") as letter_file:
    letter_contents = letter_file.read()

#Replace placeholder with name and print letters
for name in names:
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, name)
    print(new_letter)
    #Save the new letter
    with open(f"ReadyToSend/letter_for_{name}.docx", mode = "w") as completed_letter:
        completed_letter.write(new_letter)