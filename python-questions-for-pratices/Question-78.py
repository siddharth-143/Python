"""
Question 78 :
    Write a program to print the running time of execution of "1 + 1"
    for 100 times.

    Hints : Use timeit() function to measure the running time.
"""

# Solution :

from timeit import Timer
t = Timer("for i in range(100) : 1 + 1")
print(t.timeit())


"""
timeit :
    This module provides a simple eay to find the execution time
    of small bits of python code 
"""

"""
Output : 
    1.6696240000000002
"""