# Python program to demonstrate basic Euclidean Algorithm

def GCD(a, b):

    if a == 0:
        return b
    return GCD(b%a, a)

a, b = 10, 15
print("GCD (",a, ",", b, ") = ", GCD(a,b))
