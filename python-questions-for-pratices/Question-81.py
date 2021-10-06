"""
Question 81 :
    Write a program to print the list removing delete even
    numbers in [5,6,77,45,22,12,24].

    Hints : Use list comprehension to delete a bunch of elements from a list.
"""

# Solution :

li = [5, 6, 77, 45, 22, 12, 24]
li = [x for x in li if x % 2 != 0]
print(li)