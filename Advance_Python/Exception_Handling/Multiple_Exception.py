# Multiple Exception

try:
    a = int(input("Enter a : "))
    b = int(input("Enter b:" ))
    c = a/b
    print(c)

except (ZeroDivisionError, NameError):
    print("division by zero")

else:
    print("All Done")