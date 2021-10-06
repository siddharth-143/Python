"""
Question 18 :
    A website requires the user to input username and password
    to register. Write a program to check the validity of password
    input by user. Following are the criteria for checking the password.

    1. At least 1 letter between [a - z]
    2. At least 1 letter between [A - Z]
    3. At least 1 number between [0 - 9]
    4. At least 1 character from [!@#$%^&*()_+]
    5. Minimum length of transaction password : 6
    6. Maximum length of transaction password : 12. Your program should accept
    a sequence of comma separated password and will check them according to
    the above criteria. Passwords  that match the criteria are to be
    printed, each separated by a comma. Example if the following
    password are given as input to the program: ABd1234@1, aF1#2, 2w3e*, 2We3345
    Then, the output to the [rogram : ABd1234@1

    Hints : In case of input data being supplied to the question,
    it should be assumed to be a console input.
"""

# Solution :

import re

values = []
password = input("Enter a password : ")
items = [x for x in password.split(",")]

for p in items:
    if len(p) < 6 or len(p) > 12:
        continue
    else:
        pass
    if not re.search('[a-z]', p):
        continue
    elif not re.search('[A-Z]', p):
        continue
    elif not re.search('[0-9]', p):
        continue
    elif not re.search('[!@#$%^&*()_+]', p):
        continue
    elif re.search("\s", p):
        continue
    else:
        pass
    values.append(p)
print(",".join(values))