# Exercise 23 : Hanman Excercise :: Part 2 Guess Letters

'''This exercise is Part 2 of 3 of the Hangman exercise series. 
The other exercises are: Part 1 and Part 3.

Let’s continue building Hangman. 
In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter. 
The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly. 
For now, let the player guess an infinite number of times until they get the entire word. As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again. 
Remember to stop the game when all the letters have been guessed correctly! 
Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.'''

from pick_word import Pick_word
from sys import stdout

def Guess_letters():
    random_word = Pick_word()
    # cheet for check
    print(random_word)
    print(">>> Welcome to Hangman!")
    print("_ " * len(random_word))
    while True:
        guess_letter = input("\n>>> Guess ypur letter: ")
        if guess_letter in random_word:
            for charactor in random_word:
                if guess_letter == charactor:
                    stdout.write(guess_letter+" ")
                else:
                    stdout.write("_ ")
        else:
            stdout.write("Incorrect!\n")
            continue
if __name__ == "__main__":
    print("This is just one solution to the part2, in hangman the method will be overwrited.")
    Guess_letters()