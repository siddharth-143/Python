# Abstract class , Abstract method and concrete method

from abc import ABC, abstractmethod

class DefenceForece(ABC):

    @abstractmethod
    def area(self):
        pass

    def gun(self):
        print("Gun : AK47")

class Army(DefenceForece):
    def area(self):
        print("Area : Land")

class AirForce(DefenceForece):
    def area(self):
        print("Area : Air")

class Navy(DefenceForece):
    def area(self):
        print("Area : Water")

a = Army()
a.area()
a.gun()
print()

af = AirForce()
af.area()
af.gun()
print()

n = Navy()
n.area()
n.gun()