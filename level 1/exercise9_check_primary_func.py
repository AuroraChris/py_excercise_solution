# Exercise 9 : Check_Primary_Function

'''Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. 
Take this opportunity to practice using functions, described below.'''

num = int(input("Please input a number : "))
divisors = [ele for ele in range(1,num + 1) if num % ele == 0]
if (num == 1 or len(divisors) == 2):
    print("It is a prime number!")