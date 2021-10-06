"""
Question 5 :
    Define a class which has at least two method:
    get_string: to get a string from console input
    show_string: to print the string in upper case.
    Also please include simple test function to test the class method.

    Hints : Use init method to construct some parameter
"""

# Solution:

class test(object):
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("Enter a string : ")

    def show_string(self):
        print(self.s.upper())

t = test()
t.get_string()
t.show_string()

"""
Output : 
    Enter a string : abcd
    ABCD
"""