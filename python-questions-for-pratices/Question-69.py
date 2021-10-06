"""
Question 69 :
    Write a binary search function which searches an item in a sorted list.
    The function should return the index of elements to be searched in the list.

    Hints : Use if/elif to deal with condition
"""

# Solution :

import math


def binary_search(li, ele):
    bottom = 0
    top = len(li) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int(math.floor((top + bottom) / 2.0))
        if li[mid] == ele:
            index = mid
        elif li[mid] > ele:
            top = mid - 1
        else:
            bottom = mid + 1

    return index


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ele = int(input("Enter a number : "))
print(binary_search(li, ele))

"""
Output :
    Enter a number : 5
    4
    
    Enter a number : 33
    -1
    
"""

"""
floor() :
    The floor() method returns the floor of x 
    i.e the largest integer not greater than X.
    
    Example : print("math.floor(-45.17)")
    
    Output : -46
"""