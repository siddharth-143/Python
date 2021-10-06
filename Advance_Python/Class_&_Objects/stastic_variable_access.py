class test:
    a=10
    def __init__(self):
        print('a :',self.a)
        print('a :',test.a)
    def m1(self):
        print('a :',self.a)
        print('a :',test.a)
    @classmethod
    def m2(self):
        print('a :',self.a)
        print('a :',test.a)
    @classmethod
    def m3(self):
        print('a :',test.a)

t1=test()
print(' access outside the class by class name -> a :',test.a)
print(' access outside the class by using object -> a :',t1.a)
t1.m1()
t1.m2()
t1.m3()
