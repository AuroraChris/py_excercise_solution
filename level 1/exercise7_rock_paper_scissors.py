# Exercise 7 : Rock Paper Scissors

'''Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock'''

inputs = ["rock", "paper", "scissors"]
def input_and_chk():
    while True:
        p = input("Player's pick : ")
        if (p not in inputs):
            print("Please enter rock, paper, or scissors.")
        else:
            return p

while True:
    p1 = input_and_chk()
    p2 = input_and_chk()
    if (p1 == "rock" and p2 == "paper"):
        print("p2 wins!")
    if (p2 == "rock" and p1 == "paper"):
        print("p1 wins!")
    if (p1 == "rock" and p2 == "scissors"):
        print("p1 wins!")
    if (p2 == "rock" and p1 == "scissors"):
        print("p2 wins!")
    if (p1 == "paper" and p2 == "scissors"):
        print("p2 wins!")
    if (p2 == "paper" and p1 == "scissors"):
        print("p1 wins!")
    if (p1 == p2):
        print("Draw!")
    again = input("Do you want to try again ? y/N [y]")
    if (again == "N"):
        break