class test:
    def sum(self,*a):
        total=0
        for i in a:
            total=total+i
        print('sum :',total)
t1=test()
t1.sum(10,20,30)
t1.sum(10,20)
t1.sum()
