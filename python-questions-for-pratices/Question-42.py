"""
Question 42 :
    Write a program to generate and print another tuple
    whose values are even numbers in the given tuple
    (1,2,3,4,5,6,7,8,9,10)

    Hints : Use for to iterate the tuple use tuple()
    to generate a tuple from a list.
"""

# Solution :

tp = (1,2,3,4,5,6,7,8,9,10)
l = list()
for i in tp:
    if i%2 == 0:
        l.append(i)

tp2 = tuple(l)
print(tp2)

"""
Output :
    (2, 4, 6, 8, 10)
    
    Process finished with exit code 0
"""