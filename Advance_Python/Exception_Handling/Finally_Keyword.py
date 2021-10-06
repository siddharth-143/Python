# Finally Keyword

try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    c = a / b
    print(c)

except ZeroDivisionError:
    print("Division by zero")

else:
    print("Else Block")

finally:
    print("Final block always execute")