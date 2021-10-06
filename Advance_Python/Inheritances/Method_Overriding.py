# Method Overriding

class Add:
    def result(self, x, y):
        print("Addtion : ", x+y)

class Multiplication(Add):
    def result(self, a, b):
        super().result(100, 20)
        print("Multiplication : ", a*b)

m = Multiplication()
m.result(10, 20)