# Python program to demonstract hierarchical inheritance

class number :
    def __init__(self) :
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

class average(number) :
    def disp(self) :
        add = self.a + self.b + self.c +self.d
        avg = add/4
        print('Additon :', avg)

class multiplication(number) :
    def show(self) :
        result = self.a * self.b * self.c * self.d
        print('Multiplicaation :', result)

a1 = average()
a1.disp()
a2 = multiplication()
a2.show()
