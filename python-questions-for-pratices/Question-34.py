"""
Question 34 :
    Define a function which can generate a dictionary where the
    keys are numbers between 1 and 20 (both include) and the are
    square of keys. The function sholude just print the values only.

    Hints : Use dict[key] = value patter to put entry into a dictionary.
    use range() for loops. Use keys() to iterate keys in the dictionary.
    Also we canuse item() to get key/value pairs.
"""

# Solution :

num = int(input("Enter a num : "))
def print_dict():
    d = dict()
    for i in range(1, num + 1):
        d[i] = i**2

    for (k,v) in d.items():
        print(v, end=" ")

print_dict()


"""
Output :
    Enter a num : 21
    1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400 441 
    Process finished with exit code 0
"""