# Exercise 9 : Guessing Game One

'''Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.'''

from random import randint
print("Wating to generate an rand integer between 1-9...")
a = randint(1, 9)
print("Finished!")
while True:
    ipt = input("Please input a number between 1-9 : ")
    try:
        if (int(ipt) < a):
            print("Too low! Enter exit to exit the game")
        if (int(ipt) > a):
            print("Too high! Enter exit to exit the game")
        if (int(ipt) == a):
            print("You win, a new game has started! Enter exit to exit the game")
            a = randint(1, 9)
    except ValueError:
        if (ipt == "exit"):
            break