# Sebastian Boyer - Second Consolidation Project

import os
import random

# this is the function that I have created to come up with my secret word and my word bank
def word_bank():
    word_bank = ["raise", "scare", "point", "least", "trace"]
    return random.choice(word_bank)

# this is going to be the function for the gameplay. It will include what is printed out and how the game goes along.
def gameplay():
    secretWord = word_bank # this is how the secret word is chosen
    print("This is the word hunting game! \n")
    numberOfPlayers = int(input("Enter number of players: "))
    players = [f"Players {i + 1}" for i in range (numberOfPlayers)]

    # now I am going to create the variables for how we are going to track letter and word guesses
    letterGuesses = 0 # variable for letter guesses
    wordGuesses = 0 # variable for word guesses


    while True:
        for player in players:
            print(f"\n{player}'s turn:")
            guess = input("Enter a letter guess: ").lower()

    