"""
Question 31:
    Define a function that can accept an integer number as input
    and print the "It is a even number" if the number is even,
    otherwise print "it is an odd number".

    Hints : Use % operator to check if a number is even or odd.
"""

# Solution :

num = int(input("Enter a number : "))
def print_value(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")

print_value(num)

"""
Output : 
    Enter a number : 2
    Even
    
    Enter a number : 3
    Odd
"""