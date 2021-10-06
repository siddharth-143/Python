"""
Question 64 :
    The Fibonacci sequence is computed based on the following formula :

    f(n) = 0 if n = 0
    f(n) = 1 if n =1
    f(n) = f(n - 1) + (n - 2) if n > 1

    Example: If the following n is given as input to the program: 7

    Then, the output of the program should be : 13

    In case of input data begin supplied to the question,
    it should be assumed to be a console input.

    Hints : We can define recursive function in python.
"""

# Solution :

def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n - 1) + f(n - 2)


n = int(input("Enter a number : "))
print(f(n))

"""
Output :
    Enter an number : 7
    13
"""
