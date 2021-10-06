# Python program to demonstract fibonacci num :

n = int(input('Enter a number : '))
x = 0
y = 1
fib = 0
while fib < n :
    fib = fib + 1
    z = x + y
    print(z)
    x = y
    y = z
