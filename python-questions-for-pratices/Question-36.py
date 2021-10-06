"""
Question 36 :
    Define a function which can generated and print a list where the
    values are square of numbers between 1 and 21 (both include).

    Hints : Use ** operator to get power of a number. Use range()
    for loop. Use list.append to add values into a list.
"""

# Solution :

num = int(input("Enter a number : "))
def print_list():
    l = list()
    for i in range(1, num + 1):
        l.append(i**2)
    print(l)

print_list()

"""
Output : 
    Enter a number : 20
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    
    Process finished with exit code 0

"""