"""
Question 52 :
    Define a class rectangle which can be constructed by a
    length and width. The rectangle class has a method the area.

    Hints : Use def method_name(self) to define a method.
"""

# Soltion :

class rectangle():
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length * self.breadth

r = rectangle(10, 20)
print(r.area())

"""
Output :
    200
"""