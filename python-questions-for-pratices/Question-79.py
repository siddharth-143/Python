"""
Question 79 :
    Write a program to shuffle and print the list [3,6,7,8].

    Hints : Use shuffle() function to shuffle a list.
"""

# Solution :

from random import shuffle

li = [3, 6, 7, 8]
shuffle(li)
print(li)


"""
shuffle() : 
    It is used to shuffle a sequence (list). Shuffle means
    changing the position of the elements of the sequence.
    
Note : the shuffle() method cannot be used to shuffle immutable datatypes like string
"""

"""
Output : 
    [6, 3, 7, 8]
"""