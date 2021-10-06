# Thread child class with constructor

from threading import Thread

class Mythread(Thread):

    def __init__(self):     # constructor
        print("Child class constructor")
        Thread.__init__(self)       # call constructor in child class

    def run(self):      # thread class method get automatically call when thread stared
        for i in range(5):
            print("Child Thread")

t = Mythread()
t.start()
t.join()

for i in range(5):
    print("Main Thread")