

#import pickle
'''class employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno;
        self.ename = ename;
        self.esal = esal;
        self.eaddr = eaddr;
    def display(self):
        print(self.eno, '\t', self.ename, '\t', self.esal, '\t', self.addr,)

with open('emp.dat','wb') as f :
    e = employee(100,'aaa',00,'solapur')
    pickle.dump(e,f)
    print('Pickling employee object complete...')

with open('emp.dat','rb') as f :
    obj = pickle.load(f)
    print('Printing employee information after unpickling')
    obj.display'''



# Program of writing multiple employee objects to the file :

import pickle
class employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno;
        self.ename = ename;
        self.esal = esal;
        self.eaddr = eaddr;
    def display(self):
        print(self.eno, '\t', self.ename, '\t', self.esal, '\t', self.eaddr,)

f = open("emp.dat",'wb')
n = int(input('Enter employee number :'))
for i in range(n):
    eno = int(input('Enter employee id number :'))
    ename = input('Enter employee name :')
    esal = float(input('Enter employee salary :'))
    eaddr = input('Enter employee address :')
    e = employee(eno,ename,esal,eaddr)
pickle.dump(e,f)
print('Employye object pickled successfully')
f.close()

f1 = open('emp.dat','rb')
print('Employee details :')
while True :
    try :
        obj = pickle.load(f1)
        obj.display()
    except EOFError:
        print('All employee complete')
        break
f1.close()
