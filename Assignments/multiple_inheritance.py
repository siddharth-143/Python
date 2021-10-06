
# Python program to demonstrate multipe inheritance

# Base class 1

class mother :
    mothername = ''
    def mother(self) :
        print('self.mothername')

# Base class 2

class father :
    fathername = ''
    def father(self) :
        print('self.fathername')

# Derived class

class son(mother,father) :
    def parent(self) :
        print('Mother :',self.mothername)
        print('Father :',self.fathername)

# Driver's code

d1 = son()
d1.mothername = 'PUSHPA'
d1.fathername = 'SUBHASH'
d1.parent()
