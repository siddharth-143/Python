"""
Question :
    Define a function which can generated a list where the
    values are square of numbers between 1 and 20 (both included).
    Then the function need to print the first 5 elements ih the list.

    Hints : Use **operator to get power of a number. Use range
    list.append() to add values into a list. Use [n1:n2] to slice a list.
"""

# Solution :

num = int(input("Enter a number : "))
def print_list():
    l = list()
    for i in range(1, num +1):
        l.append(i**2)
    print(l[:5])
print_list()

"""
Output :
    Enter a number : 20
    [1, 4, 9, 16, 25]
    
    Process finished with exit code 0
"""