"""
Question 62 :
    Write a program to compute 1/2+2/3+3/4+........n/n+1 with a given
    n input by console (n > 0).

    Example : If the following n is given as input to the program : 5

    Then, the output of the program should be : 3.55

    In case of input data begin supplied to the question,
    it should be assumes to be a console input.

    Hints : Use float() to convert an integer to a float.
"""

# Solution :

num = int(input("Enter a number : "))
sum = 0.0
for i in range(1, num + 1):
    sum += (float(i) / (i + 1))
print(sum)

"""
Output :
    Enter a number : 5
    3.5500000000000003
"""