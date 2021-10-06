# Raise exception with message

try:
    age = int(input("Enter the age : "))
    if age < 18:
        raise ValueError("Age should be greater than or equal to 18")
    else:
        print("The age is valid")
except ValueError as obj:
    print(obj)
    