"""
Question 26 :
    Define a function which van computer the sum of two
    number.

    Hints : Define a function with two numbers as arguments.
    You can compute the sum in the function and return the value.
"""

# Solution :

num1 = int(input("Enter a 1st num : "))
num2 = int(input("Enter a 2nd num : "))

def sum(num1, num2):
    return num1 + num2

print("Total : ", sum(num1, num2))

"""
Output : 
    Enter a 1st num : 1
    Enter a 2nd num : 2
    Total :  3
"""