"""
Question 1 :
    Write a program which will find all such numbers which are divisible
    by 7 but are not a multiple 0f 5, between 1 and 100 (both included).
    The number be printed in a comma separated sequence on a single line.

    Hints : Consider use range(#begin, #end)
"""
# Solution :

l = []
for i in range(1, 100):
    if i%7 == 0 and i%5 != 0:
        l.append(str(i))

print(','.join(l))

"""
Output : 
    7,14,21,28,42,49,56,63,77,84,91,98
"""