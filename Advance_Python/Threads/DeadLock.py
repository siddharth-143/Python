# Python progrtam to implement dead lock

from threading import *
import time

l = Lock()


def hello():
    for i in range(2):
        l.acquire()
        print("From Hello Function")
        time.sleep(2)


def Nice():
    for i in range(2):
        l.acquire()
        print("From Nice Function")
        time.sleep(2)
        l.release()


t1 = Thread(target=hello)

t2 = Thread(target=Nice)

t1.start()
t2.start()