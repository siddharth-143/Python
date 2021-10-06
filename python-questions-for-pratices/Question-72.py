"""
Question 72 :
    Write a program to output a random number, which is divisible by
    5 and 7, between 0 and 10 inclusive using random module and list comprehension.

    Hints : Use random.choice() to a random elements from a list,
"""

# Solution :

import random
print(random.choice([i for i in range(201) if i % 5 == 0 and i % 7 == 0]))

# Note : Evey time when you run the program the random output is generated.

"""
Output : 
    70
"""