# Creating a thread by creating child class to thread class

from threading import Thread

class Mythread(Thread):         # child of thread
    def run(self):
        for i in range(5):
            print("Child Thread")

t = Mythread()
t.start()
t.join()        # join

for i in range(5):
    print("Main Thread")