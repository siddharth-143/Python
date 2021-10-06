"""
Question 75 :
    Write a program to randomly generated a list with 5 numbers,
    which are divisible by 5 and 7, between 1 and 1000 inclusive.

    Hints : Use random.sample() to generate a list of random values.
"""

# Solution :

import random
print(random.sample([i for i in range(1, 1001) if i % 5 == 0 and i % 7 == 0], 5))

# Note : Evey time when you run the program the random output is generated.

"""
Output : 
    [180, 162, 130, 186, 152]
"""