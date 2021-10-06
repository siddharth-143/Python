# Interface

from abc import ABC, abstractmethod

class DefenceForce(ABC):

    @abstractmethod
    def gun(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Army(DefenceForce):

    def gun(self):
        print("Gun : AK47")

    def area(self):
        print("Area : Land")

class AirForce(DefenceForce):

    def gun(self):
        print("Gun : M416")

    def area(self):
        print("Area : Air")

class Navy(DefenceForce):

    def gun(self):
        print("Gun : AWM")

    def area(self):
        print("Area : Water")

a = Army()
af = AirForce()
n = Navy()

a.area()
a.gun()
print()

af.area()
af.gun()
print()

n.area()
n.gun()