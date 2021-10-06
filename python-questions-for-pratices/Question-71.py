"""
Question 71 :
    Write a program to output a random c=even number
    between 0 and 10 inclusive using randi=om module and list comprehensive.

    Hints : Use random.choice() to a random elements from a list.
"""

import random
print(random.choice([ i for i in range(11) if i%2 == 0]))

# Note : Evey time when you run the program the random output is generated.

"""
Output :
    10
"""