"""
Question 56 :
    Define a custom exception class which takes a string message as attribute.

    Hints : To define a custom exception, we need to define a class inherited from exception.
"""

# Solution :

class my_error(Exception):
    """
    My own exception class

    Attributes :
        msg  -- explanation of the error
    """
    def __init__(self, msg):
        self.msg = msg

error = my_error("Something went erong")
print(error)