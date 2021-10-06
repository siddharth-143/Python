"""
Question 33 :
    Define a function which can print a dictionary where the key
    are numbers between 1 and 20 (both included) and the value
    are square of keys.

    Hints : Use dict[key] = value patter to put entry into a
    dictionary. Use** operator to get power of a number.
    Use range() for loops.
"""

# Solution :

num = int(input("Enter a number : "))
def print_dic():
    d = dict()
    for i in range(1, num+1):
        d[i] = i**2
    print(d)

print_dic()

"""
Output :
    Enter a number : 21
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49,
     8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256,
     17: 289, 18: 324, 19: 361, 20: 400, 21: 441}
"""