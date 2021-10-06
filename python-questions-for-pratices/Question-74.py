"""
Question 74 :
    Write a program to randomly generate a list with 5 even numbers
    between 100 and 200 inclusive.

    Hints : Use random.sample() to generate a list of random values.
"""

# Solution :

import random
print(random.sample([i for i in range(100, 201) if i % 2 == 0], 5))

# Note : Evey time when you run the program the random output is generated.

"""
Output :
    [180, 162, 130, 186, 152]
"""