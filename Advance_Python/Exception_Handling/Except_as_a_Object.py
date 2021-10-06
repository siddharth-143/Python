# Except as a object

try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a / b
    print(c)

except ZeroDivisionError as obj:
    print("Error")
    print(obj)
else:
    print("Else Block")