# Python program to demonstract multiple inheritances

class a :
    def __init__(self) :
        self.ename = 'abc'
        self.eid = 123
        print('Employee name :',self.ename)
        print('Employee id :',self.eid)

class b :
    def show(self) :
        self.eage = 46
        self.sal = 798798
        print('Employee age : ',self.eage)
        print('Employee salay :',self.sal)

class c(a,b) :
    def __init__(self):
        super().__init__()
    def dis(self) :
        print('Empployee information complete.......!')
        
a1 = c()
a1.show()
a1.dis()
