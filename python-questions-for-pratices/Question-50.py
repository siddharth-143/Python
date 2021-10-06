"""
Question-50 :
    Define a class named India and its subclass Delhi.

    Hints : Use class subclass(parentclass) to define a subclass.
"""


# Solution :

class India(object):
    pass

class Delhi(India):
    pass

i = India()
d = Delhi()
print(i)
print(d)

"""
Output :
    <__main__.India object at 0x000001BA4D8DB1C0>
    <__main__.Delhi object at 0x000001BA4D8DB7C0>
"""