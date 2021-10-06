"""
Question 89 :
    Define a class person ans its two child classes : male and female
    All classes have a method "get_gender"  which can print "male"
    for male class and "female" for female class.

    Hints : Use subclass(parameters) to define a child class.
"""

# Solution :

class persent(object):
    def get_gender(self):
        return "unknown"

class male(persent):
    def get_gender(self):
        return "Male"

class female(persent):
    def get_gender(self):
        return "Female"

m = male()
f = female()
print(m.get_gender())
print(f.get_gender())

"""
Output :
    Male
    Female
"""