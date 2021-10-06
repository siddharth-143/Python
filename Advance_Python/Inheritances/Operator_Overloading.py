
# Operator Overloading

class A:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x

class B:
    def __init__(self, x):
        self.x = x
    def __sub__(self, other):
        return self.x - other.x

a = A(1100)
b = B(200)

print(a + b)
print(b - a)
