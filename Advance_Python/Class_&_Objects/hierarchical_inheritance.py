class number:
    def __init__(self):
        self.a=10
        self.b=20

class addition(number):
    def add(self):
         self.c=self.a+self.b
         print('addition :',self.c)

class substraction(number):
    def sub(self):
         self.c=self.a-self.b
         print('substraction :',self.c)

class multiplication(number):
    def mul(self):
        self.c=self.a*self.b
        print('multiplication :',self.c)

class division(number):
    def div(self):
        self.c=self.a/self.b
        print('division :',self.c)

a1=addition()
a1.add()
s1=substraction()
s1.sub()
m1=multiplication()
m1.mul()
d1=division()
d1.div()







