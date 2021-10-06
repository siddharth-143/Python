"""
Question : 66
    Write a program using generator to print the even numbers
    between 0 and n in comma separated from while n is input by console.

    Example : If the following n is given as input to the program : 10

    Then, the output of the program should be :0,2,4,6,8,10

    Hints : Use yield to product the next values in generator.

    Hints : Use yield to produce the next value in generator.

    In case of input data begin supplied to the question, it
    should be assumed to be a console input.
"""

# Solution :

def even_generator(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

n = int(input("Enter a number : "))
values = []
for i in even_generator(n):
    values.append(str(i))

print(",".join(values))

"""
Output : 
    Enter a number : 10
    0.2.4.6.8,10
"""