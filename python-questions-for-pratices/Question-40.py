"""
Question-40 :
    Define a function  which can generate and print a tuple where the
    value are square of numbers between 1 and 20 (both include).

    Hints : Use **operator to get power of a number. Use range()
    forloop. Use list.append() to add values into a list.
    Use tuple() to get a tuole from a list.
"""

# Solution :

num = int(input("Enter a number : "))
def print_tuple():
    t = list()
    for i in range(1, num + 1):
        t.append(i**2)
    print(tuple(t))

print_tuple()

"""
Output : 
    Enter a number : 20
    (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)
    
    Process finished with exit code 0

"""