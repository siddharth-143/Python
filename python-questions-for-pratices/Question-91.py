"""
Question 91 :
    Write a program which accepts a string from console
    and print it in reverse order.

    Example : If the following string is given as input to the program :
    siddharth

    Then, the out[ut of the program should be :
    htrahddis

    Hints : Use list[::-1] to the iterate a list in a reverse order
"""

# Solution :

s = input("Enter a string : ")
s = s[::-1]
print(s)

"""
Output :
    Enter a string : siddharth
    htrahddis
"""