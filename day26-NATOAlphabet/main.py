#NATO Alphabet
#Ashlynn Ward, June 4, 2025
#This program converts a given word into the NATO alphabet.

#Import pandas and os libraries
import pandas
import os

#Change working directory so program can access files
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

#Generate phonetic function uses list comprehension to store the nato version of the word, and validates input
def generate_phonetic():
    try:
        word = input(f"Enter a word: ").upper()
        nato_word = [nato_alphabet[letter] for letter in word]
    except KeyError:
        print("Only letters in the alphabet, please.")
        generate_phonetic()
    else:
        #Print word
        print(nato_word)

#Open nato alphabet csv and save it as a data frame
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

#Store the dataframe as a dictionary using dictionary comprehension
nato_alphabet = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

#Prompt user to enter a word - casing doesn't matter
generate_phonetic()

