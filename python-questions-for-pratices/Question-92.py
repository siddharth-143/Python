"""
Question 92 :
    Write a program which accepts a string from console
    and print the characters that have even indexes.

    Example : If the following string is given as input to
    the program :
    H1e2l3l4o5w6o7r8l9d0

    Then, the output of the program should be :
    Hello world

    Hints : Use list[::2] to iterate a list by step 2.
"""

# Solution :

s = input("Enter a string : ")
s = s[::2]
print(s)

"""
Output :
    Helloworld 
"""