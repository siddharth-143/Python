"""
Question 93 :
    Write a program which prints all permutations of [1,2,3]

    Hints : Use itertools.permutations() to get permutations of list.
"""

# Solution :

import itertools
print(list(itertools.permutations([1, 2, 3])))

"""
Output :
    [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
"""