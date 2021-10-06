# Try and Except Statement - Catching Exceptions

# Python program to handle simple runtime error

try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a/b
    print(c)
except:
    print("Can't divide with zero")