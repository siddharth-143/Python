class student:
    def __init__(self):
        self.name='siddharth'
        self.roll=101
        print('in student class')
    def show(self):
        print('name :',self.name)
        print('roll no :',self.roll)

class test(student):
    def __init__(self):
        super().__init__()
        self.m=68
        self.n=90
        print('in test class')
    def display(self):
        print('m =',self.m)
        print('n =',self.n)

class result(test):
    def grade(self):
        self.total=self.m+self.n
        self.average=self.total//2
        print('total =',self.total)
        print('average =',self.average)

r1=result()
r1.show()
r1.display()
r1.grade()

