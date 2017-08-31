# Excercise 6 : String Lists

'''Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)

'''
s = input("Please input a word : ")
if (s[::-1] == s):
    print("It is a palindrome!")