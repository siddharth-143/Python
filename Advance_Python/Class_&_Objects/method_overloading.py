class test:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print('sum of three no :',a+b+c)
        elif a!=None and b!=None:
            print('sum of two no :',a+b)
        else:
            print('provid 2 and 3 arugument')
s1=test()
s1.sum(10,20,30)
s1.sum(10,20)
s1.sum()
