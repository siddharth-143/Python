# Single tasking using a thread
from threading import Thread

class MyExam:
    def disp(self):
        self.q1()
        self.q2()
        self.q3()

    def q1(self):
        print("Question 1 Solved")

    def q2(self):
        print("Question 2 Solved")

    def q3(self):
        print("Question 3 Solved")

mye = MyExam()
t = Thread(target=mye.disp)
t.start()