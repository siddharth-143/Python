"""
Question 49 :
    Define a class named India which has a static
    method called as nationality.

    Hints : Use @staticmethod decorator to define
    class static method,
"""

# Solution :

class India():
    def nationality(self):
        print("Indian")

i = India()
i.nationality()
India.nationality(self="indian")
