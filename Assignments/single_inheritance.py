
# Python program to demonstrate single inheritance

# Base class
class parent :
    def fun1(self) :
        print('This function is in parent class')

# Derived class
class child(parent) :
    def fun2(self) :
        print('This function is in child class')

# Driver's code
obj = child()
obj.fun1()
obj.fun2()
