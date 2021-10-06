# Python program to demonstract single inheritance

class a :
    def __init__(self) :
        self.a = int(input('Enter a length :'))
        self.b = int(input('Enter a breath :'))

class b(a) :
    def cal(self) :
        result = self.a * self.b
        print('Area of reactangle :',result)

a1 = b()
a1.cal()
