# Exercise 21 : Guess Game V2

'''In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess. 
A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. 
But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. 
After you’ve written the program, try to find the optimal strategy! (We’ll talk about what is the optimal one next week with the solution.)'''

guess_list = [0, 100]
def guess(num=100):
    guess_num = num // 2
    guess_list.append(guess_num)
    guess_list.sort()
    result = input("I guess its {0}, you just input high, low, and yes : ".format(guess_num))
    if result == "yes":
        print("haha")
    if result == "high":
        left = guess_list[guess_list.index(guess_num)-1]
        return guess(left + guess_num)
    if result == "low":
        right = guess_list[guess_list.index(guess_num)+1]
        return guess(right + guess_num)

print("This time, you come up with a number and let me guess")
ipt = input("Please come up with a number 1-100, input start when you want to start the game : ")
if ipt == "start":
    guess()