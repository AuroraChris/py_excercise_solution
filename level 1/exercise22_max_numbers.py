# Excercise 22 : Max Of Three

'''Implement a function that takes as input three variables, and returns the largest of the three. 
Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python normally takes care of for us. 
All you need is some variables and if statements!'''

l = []
def maxnum(l):
    m = l[0]
    for i in l:
        if i > m:
            m = i
    print(m)

#max = 50
maxnum([20,50,40])