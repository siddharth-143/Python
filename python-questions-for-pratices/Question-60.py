"""
Question 60 :
    Write a program to read an ASCII string and convert it ta
    a unicode string.

    Hints : Use unicode() function to convert.
"""

# Solution :
from numpy.core import unicode

s = input("Enter a string : ")
u = unicode("utf-8", s)
print(u)

"""
Output :
    code doesn't work
    If you know the solution. 
    let me know....
"""