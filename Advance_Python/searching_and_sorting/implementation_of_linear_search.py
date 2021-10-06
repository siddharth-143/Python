def linear_search(alist, key):
    """ Return index of key in alist . Return -1 if key not present."""
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1

alist = input("Enter the list of numberd :")
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input("Enter a number to be search : "))

index = linear_search(alist, key)
if index < 0:
    print("{} wad not found ".format(key))
else:
    print("{} was found at index {}".format(key,index))

"""
    The "format()" method formats the specified value(s) and insert them inside the string's placeholder {}.
    
    The format() method returns the formatted string.
    
    Syntax :
        string.format(value1, value2)
"""