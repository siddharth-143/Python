"""
Question 41 :
    Given a tuple(1,2,3,4,5,6,7,8,9,10), write a program
    to print the first half values in one line and the last
    half values in one line.

    Use [n1:n2] notation to get a slice from a tuple.
"""

# Solution :

tp = (1,2,3,4,5,6,7,8,9,10)
tp1 = tp[:5]
tp2 = tp[5:]
print(tp1)
print(tp2)

"""
Output :
    (1, 2, 3, 4, 5)
    (6, 7, 8, 9, 10)

Process finished with exit code 0

"""