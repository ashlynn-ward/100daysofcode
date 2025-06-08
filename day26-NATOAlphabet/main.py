#NATO Alphabet
#Ashlynn Ward, June 4, 2025
#This program converts a given word into the NATO alphabet.

#Import pandas library
import pandas

#Open nato alphabet csv and save it as a data frame
alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

#Store the dataframe as a dictionary using dictionary comprehension
nato_alphabet = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

#Prompt user to enter a word - casing doesn't matter
word = input(f"Enter a word: ").upper()

#Use list comprehension to store the nato version of the word
nato_word = [nato_alphabet[letter] for letter in word]

#Print word
print(nato_word)