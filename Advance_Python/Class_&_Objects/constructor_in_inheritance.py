# counstructor in inheritances
class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print('base class constructor')
    def show(self):
        print('a =',self.a)
        print('b =',self.b)

class B(A):
    def __init__(self,m,n):
        super().__init__(m,n)
        self.c=30
        print('derived constructor')
    def display(self):
        print('derived class method ')
        print('c =',self.c)

b1=B(10,20)
b1.show()
b1.display()

