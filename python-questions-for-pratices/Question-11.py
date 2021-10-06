"""
Question 11 :
    Write a program which accepts a sequence of comma separated
    4 digit binary numbers as its input and then check whether
    they are divisible by 5 or not. The numbers that are divisible
    by 5 are to be printed in a comma separated sequence.
    Example : 0100,0011,1010,1001 then the output should be : 1010
    Notes: Assume the data is input by console.

    Hints : In case of input data begin supplied to the question,
    it should be assume to be a console input.
"""

# Solution :

value = []
num = input("Enter a number : ") 
items = [x for x in num.split(",")]
for i in items:
    inti = int(i, 2)
    if not inti % 5:
        value.append(i)

print(",".join(value))

"""
Output : 
    Enter a number :  0100,0011,1010,1001
    1010
"""