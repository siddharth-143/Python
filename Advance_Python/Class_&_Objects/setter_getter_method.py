class student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMark(self,mark):
        self.mark=mark
    def getMark(self):
        return self.mark

num=int(input('enter a no of students :'))
for i in range(num):
    s=student()
    name=input('enter a name :')
    s.setName(name)
    mark=int(input('enter a mark :'))
    s.setMark(mark)
    print('name :',s.getName())
    print('mark :',s.getMark())
    print()
