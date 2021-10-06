"""
Question 35 :
    Define a function which can generated a dictionary where the keys
    are numbers between 1 and 20 (both included) and the values are square
    of keys. The function should just print the keys only.

    Hints : Use dict[keys] = value pattern to put entry into a dictionary.
    Use range() for loops. Use keys() to iterate keys in the dictionary.
    Also we can use item() to get keys/values pairs.
"""

# Solution :

num = int(input("Enter a number : "))
def print_dict():
    d = dict()
    for i in range(1, num+1):
        d[i] = i**2

    for j in d.keys():
        print(j, end=" ")

print_dict()

"""
Output : 
    Enter a number : 21
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 
    Process finished with exit code 0

"""