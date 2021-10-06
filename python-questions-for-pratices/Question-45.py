"""
Question 45 :
    Write a program which can map() to make a list whose
    elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

    Hints : Use map() to generate a list.
    Use lambda to define anonymous functions.
"""

# Solution :

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = map(lambda x: x**2, li)
print(list(square))

"""
Output : 
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    
    Process finished with exit code 0

"""