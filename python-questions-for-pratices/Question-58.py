"""
Question 58 :
    Write a program which accepts a sequence of words separated
    by whitespace as input to print the words compose of digits only.

    Example : If the following words is given as input to the program :
    2 cats and 3 dogs.

    Then, the output of the program should be :
    ['2', '3']

    In case of input data begin supplied to the question,
    it should be assumed to be a console input.

    Hints : Use re.findall() to fins all substring using regex.
"""

# Spolution :

import re
s = input("Enter a string : ")
print(re.findall("\d+", s))

"""
Output :
    Enter a string : 2 cats and 3 dogs
    ['2', '3']
"""