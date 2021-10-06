"""
Question  48 :
    Write a program which can map() to make a list whose
    elements are square of numbers between 1 and 20 (both included).

    Hints : Use map() to generate a list.
    Use lambda to define anonymous function.
"""

# Solution :

num = int(input("Enter a num : "))
even_num = map(lambda x: x % 2 == 0, range(1, num + 1))
print(list(even_num))

"""
Output : 
    Enter a num : 20
    [False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]
    
    Process finished with exit code 0
"""
