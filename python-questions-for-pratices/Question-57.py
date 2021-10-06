"""
Question 57 :
    Assuming that we have some email addresses in the
    "username@companyname.com" format.
    Write a program to print the user name of a given email address.
    Both user names and company names are composed of letters only.

    Example : if the following email address is given as input to the program :
    john@google.com
    Then, the output of the program should be :
    jonh

    In case of input data begin supplied to question, it should be
    assumed to be a console input.

    Hints : Use \w to match letters.
"""

# Solution :

import re

email_add = input("Enter a email id : ")
f1 = ("(\w+)@((\w+\.)+(com))")
r2 = re.match(email_add,f1)
print(r2.group(1))
