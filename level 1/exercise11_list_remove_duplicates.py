# Exercise 11 : List Remove Duplicates

'''Write a program (function!) that takes a list and returns a new list 
that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''

def without_sets(*args):
    l = []
    for ele in args:
        if ele not in l:
            l.append(ele)
    print(l)

def with_sets(*args):
    print(set(args)) 

without_sets(1,1,2,2,3,3)
with_sets(1,1,2,2,3,3)