#Caesar Cipher
#Ashlynn Ward, May 6, 2025
#This program enocdes and decodes messages using the Caesar cipher. It prompts the user to enter
#how many spaces to shift each letter. 

#Define a list of all letters in the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Function encrypt will shift the letters of a message forward by the specified number 
def encrypt(original_text, shift_num):
    #Define empty string to store encrypted message
    encrypted_text = ""
    #Shift each letter
    for letter in original_text:
        #If character is in alphabet, find its index in the alphabet list and add new letter to decryption
        if letter in alphabet:
            index = alphabet.index(letter)
            encrypted_text+=alphabet[index-shift_num]
        #If character is not in alphabet list, add character to the decryption
        else:
            encrypted_text+=letter
    print(f"Here is the decoded message: {encrypted_text}")

#Function decrypt will shift the letters of a message backward by the specified number
def decrypt(original_text, shift_num):
    #Define empty string to store encrypted message
    decrypted_text = ""
    #Shift each letter
    for letter in original_text:
        #If character is in alphabet, find its index in the alphabet list and add new letter to decryption
        if letter in alphabet:
            index = alphabet.index(letter)
            decrypted_text+=alphabet[index-shift_num]
        #If character is not in alphabet list, add character to the decryption
        else:
            decrypted_text+=letter
    print(f"Here is the decoded message: {decrypted_text}")

#Function caesar determines whether encrypt or decrypt should be used
def caesar(direction, original_text, shift_num):
    if direction == "encode":
        encrypt(original_text, shift_num)
    elif direction == "decode":
        decrypt(original_text, shift_num)

#Print greeting
print("Welcome to the Caesar Cipher.")

#Prompt user to choose encoding or decoding, then enter their message and shift number
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Call caesar function
caesar(direction, text, shift)

#Continue program until user enters "no"
continue_cipher = "yes"
while continue_cipher!="no":
    continue_cipher = input("Type 'yes' if you want to go again. Otherwise, type 'no'.")
    #If "yes is entered, run cipher again"
    if continue_cipher == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)
    #If "no" is entered, end program
    elif continue_cipher == "no":
        print("Thank you for using the Caesar Cipher!")
        continue
    #Otherwise, prompt user to enter "yes" or "no" again
    else:
        print("Invalid option chosen.")
