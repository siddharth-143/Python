"""
Question 86 :
    By using list comprehension, write a program to
    print the list after removing the values 24 in
    12, 24, 35, 70, 88, 120, 155].

    Hints : Use list's remove method to delete a values.
"""

# Solution :

li = [12, 24, 35, 70, 88, 120, 155]
li = [x for x in li if x != 24]
print(li)

"""
Output :
    
"""