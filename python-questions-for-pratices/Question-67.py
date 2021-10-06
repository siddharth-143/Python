"""
Question 67 :
    Write a program using generator to print the numbers which can be
    divisible by 5 and 7 between 0 and n in comma separated form while
    n is console input.

    Example : If the following n is input to the program : 100

    Then, the output of the program should be : 0, 35, 70

    Hints : Use yield to produce the next values in generator

    In case of input beging supplied to the question, it should be
    assumed to be a console input.
"""

# Solution :

def num_div(n):
    for i in range(n + 1):
        if i%5 == 0 and i%7 == 0:
            yield i

n = int(input("Enter a number : "))
values = []
for i in num_div(n):
    values.append(str(i))

print(",".join(values))

"""
Output : 
    Enter a number : 100
    0,35,70
"""