"""
Question 51 :
    Define a class named circle which can be constructed by a radius.
    The circle class has a method which can compute the area.

    Hints : Use def method_name(self) to define a method.
"""

# Solution :

radius = float(input("Enter a radius : "))
class circle():
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return self.r**2*3.14

c = circle(radius)
print("Area of circle : ", c.area())

"""
Output :
    Enter a radius : 5
    Area of circle :  78.5
"""