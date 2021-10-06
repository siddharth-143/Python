class addition:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        self.c=self.a+self.b
        print('addition :',self.c)

a1=addition(10,20)
a1.add()
