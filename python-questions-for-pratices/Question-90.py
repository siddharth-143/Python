"""
Question 90 :
    Write a program which count and print the numbers of each character
    in a string input by console.

    Example : If the following string is given as input to the program :
    abcdefgabc

    Then, the output of the program should be :
    a,2 c,2 b,2 e,1,d,1,g,1 f,1

    Hints : Use dict to store key/values pairs.
    Use dict.get() method to lookup a key with default values.
"""

# Solution :

dic = {}
s = input("Enter a string : ")
for s in s :
    dic[s] = dic.get(s, 0) + 1
print("\n".join(["%s,%s" % (k, v) for k, v in dic.items()]))


"""
dict.get() :
    Python dictionary method get() returns a value for the given key. 
    If key is not available then returns default values None.
"""

"""
Output :
Enter a string : abcdefgabc
    a,2
    b,2
    c,2
    d,1
    e,1
    f,1
    g,1

"""