# Try with Else Clause

try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a / b
    print(c)

except ZeroDivisionError:
    print("division by zero")

else:
    print("Else block executed")
