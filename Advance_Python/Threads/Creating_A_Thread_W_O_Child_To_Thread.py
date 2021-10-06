# Creating a thread without creating child class to thread class

from threading import Thread

class Mythread:
    def disp(self, a, b):
        print("Addition : ", a+b)

my = Mythread()
t = Thread(target=my.disp, args=(10, 20))
t.start()