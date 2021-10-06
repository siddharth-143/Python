# Python program to demonstract interface inheritance

from abc import *
class operation(ABC) :
    @abstractmethod
    def evod(self) :
        pass
    @abstractmethod
    def nepo(self) :
        pass

class demo(operation) :
    def evod(self) :
        a = int(input('Enter no to check even or odd :'))
        if a%2==0:
            print('Even')
        else :
            print('Odd')

    def nepo(self) :
        b = int(input('Enter a no to check negative or positive'))
        if b>0:
            print('Positive')
        else :
            print('Negative')

d1 = demo()
d1.evod()
d1.nepo()
