# class method

class test:
    count=0
    def __init__(self):
        test.count=test.count+1
    @classmethod
    def show(cls):
        print('the number of object create for test class',cls.count)

t1=test()
t2=test()
t3=test()
t1.show()

'''
basically i done this stuff

    class test:
    count=0
    def __init__(self):
        self.count=self.count+1

it don't get the count tobe increments        
'''
