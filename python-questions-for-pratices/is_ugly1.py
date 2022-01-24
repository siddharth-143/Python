# Python program to find n'th Ugly number

def max_div(a, b):
    while a%b == 0:
        a = a/b
    return a

def is_ugly(num):
    num = max_div(num, 2)
    num = max_div(num, 3)
    num = max_div(num, 5)
    return 1 if num == 1 else 0

def n_th(n):
    i = 1
    count = 1
    while n>count:
        i += 1
        if is_ugly(i):
            count += 1
    return i

digit = 150
num = n_th(digit)
print("Ugly number of ",digit,"is : ", num)
