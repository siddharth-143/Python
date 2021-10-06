"""
Question 23 :
    Write a method which can calculate square values of numbers.

    Hints : Using the ** operator
"""

# Solution :

num = int(input("Enter a number : "))

def square(num):
    return num ** 2

print(square(num))

"""
Output : 
    Enter a number : 5
    25
"""
