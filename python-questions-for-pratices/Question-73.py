"""
Question 74 :
    Write a program to generate a list 5 random numbers between
    100 and 200 inclusive,

    Hints : Use random.random() to generate a list of random values.
"""

# Solution :

import random
print(random.sample(range(100), 5))

# Note : Evey time when you run the program the random output is generated.

"""
sample() :
    The sample() method return a list with a randomly selection of a 
    specified number of items from a sequence,
    
    NOte : This method does not change the original sequence. 
"""

"""
Output :
    [58, 72, 48, 19, 33]
"""