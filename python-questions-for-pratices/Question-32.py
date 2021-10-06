"""
Question 32 :
    Define a function which can print a dictionary where the keys are
    numbers between 1 and 3 (both included) and the values are square
    of keys.

    Hints : Use dict[key] = values pattern to put entry into dictionary.
            Use **operator to get power of a number.
"""

# Solution :

def print_dic():
    d = dict()
    d[1] = 1
    d[2] = 2**2
    d[3] = 3**3
    print(d)
print_dic()

"""
Output :
    {1: 1, 2: 4, 3: 27}
"""