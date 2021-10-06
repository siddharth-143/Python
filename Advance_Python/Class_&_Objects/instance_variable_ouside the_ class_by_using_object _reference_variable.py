# instance variable ouside the 
# class by using object reference variable

print('''instance variable ouside the of class by using object reference variable''')

class test:
    def __init__(self):
        self.a=10
        self.b=20
    def show(self):
        self.c=30
        print('a :',self.a)
        print('b :',self.b)
        print('c :',self.c)
t1=test()
t1.show()
t1.d=40
print('d :',t1.d)
