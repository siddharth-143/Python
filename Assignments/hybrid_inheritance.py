
# Python program to demonstrate hybrid inheritance

class info :
    def __init__(self) :
        self.name = 'abc'
        self.age = 20
        self.land = 30
        print('Framer information :-')
        print('Framer name :',self.name)
        print('Framer age :',self.age)
        print('Framer land :',self.land)

class invest(info) :
    def disp(self) :
        print('Work :-')
        self.a = 3000
        print('Planting :',self.a)
        self.b = 4000
        print('For electricity :',self.b)
        self.c = 9000
        print('For cutting :',self.c)
        self.d = 7000
        print('For workers :',self.d)

class loan :
    def show(self) :
        self.e = 7000
        print('Also loan include :-')
        print('Loan is :',self.e)

class farmer(invest,loan) :
    def cal(self) :
        print('Money investment in farm :')
        self.m = self.a + self.b + self.c + self.d
        print('Investment without laon :',self.m)
        self.p = self.m +self.e
        print('Investment with loan :',self.p)

f1 = farmer()
f1.disp()
f1.show()
f1.cal()
