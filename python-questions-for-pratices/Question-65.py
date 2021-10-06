"""
Question 65 :
    The fibonacci sequence is computed based on the following formula.

    f(n) = 0 if n = 0
    f(n) = 1 if n = 1
    f(n) = (n -1) + (n - 2) if n > 0

    Write s program using list comprehension to print the
    fibonacci sequence in comma separated from with a given n input
    by console.

    Example : If the following n is given as input to the program : 7

    Then, The output of the program should be : 0,1,1,2,3,4,5,8,13

    Hints : We can define recursive function in python. Use list
    comprehension to generated a list from an exiting list.
    Use string.join() to join a list of strings.

    In case of input data being supplied to the question, it should
    be assumed to be a console input.
"""


# Solution :

def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n - 1) + f(n - 2)


n = int(input("Entre a number : "))
values = [str(f(x)) for x in range(0, n + 1)]
print(",".join(values))

"""
Output :
    Entre a number : 7
    0,1,1,2,3,5,8,13
"""