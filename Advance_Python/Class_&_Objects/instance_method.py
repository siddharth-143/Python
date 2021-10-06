# instance method
class student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def show(self):
        print('name :',self.name)
        print('mark :',self.mark)
    def grade(self):
        if self.mark>=90:
            print('A+')
        elif self.mark>=80:
            print('A')
        elif self.mark>=70:
            print('B+')
        elif self.mark>=60:
            print('B')
        elif self.mark>=50:
            print('C+')
        elif self.mark>=36:
            print('C')
        else:
            print('fail')
num=int(input('enter a number of student :'))
for i in range(num):
    name=input('enter name :')
    mark=int(input('enter mark :'))
    s=student(name,mark)
    s.show()
    s.grade()
    print()
