class test:
    def __init__(self,*a):
        print('constrctor with variable no of arguments :')

t1=test()
t2=test(10)
t3=test(10,20)
t4=test(10,20,30)

################################################################################

class test:
    def __init__(self,*a):
        print('constrctor with variable no of arguments :',*a)

t1=test()
t2=test(10)
t3=test(10,20)
t4=test(10,20,30)

#################################################################################

class test:
    def __init__(self,*a):
        self.a=a
        print('constrctor with variable no of arguments :',a)

t1=test()
t2=test(10)
t3=test(10,20)
t4=test(10,20,30)
