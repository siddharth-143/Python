"""
Question 39 :
    Define a function which can generate a list where the values are
    square of numbers between 1 and 20 (both included). Then the function
    needs to print all values except the 5 elements in the list.

    Hints : Use ** operator to get power of a number. Use range() for loops.
    Use list.append() to add values into a list. Use [n1:n2] to slice a list.
"""

# Solution :

num = int(input("Enter a number : "))
def print_list():
    l = list()
    for i in range(1, num):
        l.append(i**2)
    print(l[5:])

print_list()

"""
Output : 
    Enter a number : 20
    [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
    
    Process finished with exit code 0

"""