# Python program to demonstrate wroking of extended Euclidean Algorithm

def GCD_Extended(a, b):

    # base case
    if a == 0:
        return b,0,1
    gcd, x1, y1 = GCD_Extended(b%a, a)

    # update x and y using results of recursive call
    x = y1 - (b//a)*x1
    y = x

    return gcd, x, y
a, b = 10 ,15
g, x, y = GCD_Extended(a, b)
print("GCD Extended (", a, ",", b, ") = ",g)
