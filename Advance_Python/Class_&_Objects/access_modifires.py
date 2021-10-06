class test:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
    def show(self):
        print('a :',self.a)
        print('b :',self._b)
        print('c :',self.__c)

b1=test()
b1.show()

