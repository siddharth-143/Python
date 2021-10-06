# Python program to demonstract method overloading and overriding

# Method overloading

class test :
    def sum(self, a = None, b = None, c = None) :
        if a!= None and b!= None and c!= None :
            print('The concate of 3 char :',a+b+c)

        elif a!= None and b!= None :
            print('The concate of 2 char : ',a+b)

        else :
            print('Not provided input...')

t = test()
t.sum('a', 'b', 'c')
t.sum('A', 'B')
t.sum()

# Methid Overriding

class a :
    def shape(self) :
        print('It is circle......')

class b(a) :
    def shape(self) :
        super().shape()
        print('It is triangle..')

a1 = b()
a1.shape()
