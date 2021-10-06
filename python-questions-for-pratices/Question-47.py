"""
Question 47 :
    Write a program which can filter() to make a list whose
    elements are even number between 1 and 20 (both included).

    Hints : Use filter() to filter elements of a list.
    Use lambda anonymous function.
"""

# Solution :


even_num = filter(lambda x: x%2 == 0, range(1, 21))
print(list(even_num))

"""
Output : 
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    Process finished with exit code 0
"""