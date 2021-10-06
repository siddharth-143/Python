"""
Question 53 :
    Define a class named shape and its subclass square. The square
    class has an init function which takes a length as argument.
    Both classes have a area function which can print the area of
    the shape where shape's area is 0 by default.

    Hints : To override a method in super class, we can define a
    method with the same name in the super class.
"""

# Solution :

class shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class square(shape):
    def __init__(self, l):
        shape.__init__(self)
        self.length = l

    def area(self):
        return self.length * self.length

s = square(10)
print(s.area())

"""
Output :
    100
"""