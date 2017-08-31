# Excercise 17 : Element Search

'''Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.'''

# Approach 1
#def ele_search_withoutbs(lst, num):
    #return (num in lst)
#print(ele_search_withoutbs([1,2,3,4], 4))

#Approach 2 binary search based on tail recursion
def ele_search_withbs(lst, num):
    lst.sort()
    def binary_search(lst):
        if (len(lst) == 1 and lst[0] != num):
            return False
        if (num < lst[len(lst) // 2]):
            slc1 = lst[:len(lst) // 2]
            return binary_search(slc1)
        if (num > lst[len(lst) // 2]):
            slc2 = lst[len(lst) // 2:]
            return binary_search(slc2)
        if (num == lst[len(lst) // 2]):
            return True
        return False
    return binary_search(lst)

print(ele_search_withbs([1, 3, 5, 30, 42, 43, 500], 5))
print(ele_search_withbs([1, 3, 5, 30, 42, 43, 500], 9))