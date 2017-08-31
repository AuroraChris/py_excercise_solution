# Exercise 23 : Hanman Excercise :: Part 3 Hangman

'''This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, but to finish this exercise you will have to have finished Parts 1 and 2 or use the solutions (Part 1 and Part 2).

In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for guessing the letter and displaying that information to the user. 
In this exercise, we have to put it all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
Optional additions:

When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman. This is challenging - do the other parts of the exercise first!
Your solution will be a lot cleaner if you make use of functions to help you!'''

from pick_word import Pick_word
from sys import stdout
random_word = Pick_word()

def letter_index_list(lst, item):
    return [i for i, x in enumerate(lst) if x == item]

def Guess_letters():
    # Cheet for check
    print(random_word)
    guesses_left = 6
    print(">>> Welcome to Hangman!")
    print("_ " * len(random_word))
    guess_seq = ["_ " for i in range(len(random_word))]
    while True:
        guess_letter = input("\n>>> Guess ypur letter: ")
        if len(guess_letter) != 1 and guess_letter != "exit":
            raise ValueError("Please put only 1 charactor!")
        if guess_letter == "exit":
            return "Bye!"
        if guess_letter in random_word:
            letter_position = letter_index_list(random_word, guess_letter)
            for index in letter_position:
                guess_seq[index] = (guess_letter+" ")
            guess_word = "".join(guess_seq)
            stdout.write(guess_word+"\n")
            if "".join(guess_word.split()) == random_word:
                return "You win!"
        else:
            guesses_left = guesses_left - 1
            stdout.write("Incorrect!\nYou have {} incorrect guess left.".format(guesses_left))
            if guesses_left <= 0:
                return "\nYou lose!"
            continue
result = Guess_letters()
print(result)