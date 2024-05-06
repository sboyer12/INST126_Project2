# Sebastian Boyer - Second Consolidation Project

import os
import random

# this is the function that I have created to come up with my secret word and my word bank

def word_bank():
    word_bank = ["raise", "scare", "point", "least", "trace"]
    return random.choice(word_bank)

# this is going to be the function for the gameplay. It will include what is printed out and how the game goes along.
def gameplay():
    secretWord = word_bank() # this is how the secret word is chosen it is also a call to the word_bank() function
    print("This is the word hunting game! \n")
    numberOfPlayers = int(input("Enter number of players: "))
    players = [f"Players {i + 1}" for i in range (numberOfPlayers)]

    # now I am going to create the variables for how we are going to track letter and word guesses
    letterGuesses = {player: 0 for player in players} # variable for letter guesses
    wordGuesses = 0 # variable for word guesses

    flag = True
    while flag:
        for player in players:
            print(f"\n{player}'s turn:")
            guess = input("Enter a letter or word guess: ").lower()
            # print(str(len(guess)))
            if len(guess) == 1:
                if guess in secretWord:
                    count = secretWord.count(guess)
                    print(f"The letter {guess} appears in the secret word {count} times in the secret word. \n")
                else:
                    print(f"The letter {guess} does not appear in the secret word. \n")
                

                letterGuesses[player] += 1
            else:
                if guess == secretWord:
                    print(f"Congrats! You have won the game because the secret word was {secretWord}! Play again soon!")
                    flag = False
                if wordGuesses == 2:
                    print(f"Sorry the secret word was {secretWord}. You'll get it next time!")
                    flag = False
                wordGuesses += 1
            # here we describe the guess function. This is to depict a guess inside of the function and to see if the player has guessed the correct letter
            


        # this is the word guess section
        

       # wordGuesses += 1
    # this below is the function that we will use to run the game after it is over


def main():
    gameplay()
    
    


if __name__ == "__main__":
    main()
