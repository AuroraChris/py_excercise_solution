# Exercise 2 : Odd_Or_Even

'''Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user.

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.'''

num = int(input("Please input an number : "))
check = int(input("Please input an factor : "))

if (num % 4 == 0):
    print("It is a multiple of 4.")

if (num % check ==0):
    print("It is a multiple of %d" % check)

if (num % 2 == 0):
    print("It is an even.")
if (num % 2 == 1):
    print("It is an odd.")