"""
Question 82 :
    By using list comprehension, write a program to print the
    list after removing delete numbers which are divisible by
    5 ans 7 in [12,24,35,70,88,120,166].

    Hints : Use list comprehension to delete a bunch of element from a list.
"""

# Solution :

list = [12, 24, 35, 70, 88, 120, 166]
list = [x for x in list if x % 5 != 0 and x % 7 != 0]
print(list)

"""
Output : 
    [12, 24, 88, 166]
"""
