# pickling and unpickling

import pickle

class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address

    def disp(self):
        print(f"Name : {self.name} Rol : {self.roll} Address : {self.address}")

