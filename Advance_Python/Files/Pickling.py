# Pickling

import pickle, stu

n = int(input("Enter Number Of Student : "))
with open("student.dat", mode="wb") as f:
    for i in range(n):
        name = input("Enter student name : ")
        roll = int(input("Enter roll : "))
        address = input("Enter address : ")
        stu1 = stu.Student(name, roll, address)
        pickle.dump(stu1, f)

print("Pickling Done!!")
