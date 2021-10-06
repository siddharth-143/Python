"""
Question 68 :
    Wite a program which accepts basic mathematics expressions
    from console and print the evaluation result.

    Example : If the following string is given as input to
    the program : 35 + 3

    Then, the output of the program should be : 38

    Hints : Use eval() to evaluate an expression.
"""

# Solution :

expression = input("Enter a expression : ")
print(eval(expression))

"""
Output :
    Enter an expression : 35 + 3
    38
"""