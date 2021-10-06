"""
    Constructor Overriding
"""
class Father:

    def __init__(self):
        self.money = 1000
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):

    def __init__(self, r):
        self.money = r
        self.car = "BMW"
        print("Son class constructor")

    def disp(self):
        print("Son class instance method")


s = Son(2000)
print(s.money)
print(s.car)
s.disp()
s.show()