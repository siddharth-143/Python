# Raise exception

try:
    age = int(input("Enter the age : "))
    if age < 18:
        raise ValueError
    else:
        print("The age is valid")
except ValueError as obj:
    print("The age is not valid")
    print(obj)