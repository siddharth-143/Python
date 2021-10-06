"""
    Constructor in Inheritances
"""

class Father:
    def __init__(self, m):
        self.money = m
        print("Father class constructor")

    def show(self):
        print("Father class instance method")

class Son(Father):
    def disp(self):
        print("Son class instance method")

s = Son(1000)
print(s.money)
s.show()
s.disp()