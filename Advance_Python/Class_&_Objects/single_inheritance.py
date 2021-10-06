class A:
    def __init__(self):
        self.a=int(input('enter a 1st no :'))
        self.b=int(input('enter a 2md no :'))

class B(A):
    def calculate(self):
        self.c=self.a+self.b
        print('addition of two no :',self.c)

b1=B()
b1.calculate()
