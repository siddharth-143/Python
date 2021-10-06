# Daemon Thread

from threading import Thread, current_thread
from time import sleep

# def disp():
#     print("Disp Function")
#     t2 = Thread(target=show)
#     print("T2 : ", t2.isDaemon())
#     t2.start()

# def show():
#     print("Show Function")
#
# mt = current_thread()
# print(mt.getName())
# print("MT : ", mt.isDaemon())
#
# t1 = Thread(target=disp)
# print("Before T1 : ", t1.isDaemon())
# t1.setDaemon(True)
# print("After T1 : ", t1.isDaemon())
# t1.start()
# t1.join()

def teacher():
    for i in range(1, 10):
        print("Teaching Session", i)
        sleep(1)

t1 = Thread(target=teacher)
t1.setDaemon(True)
t1.start()
sleep(6)
print("Exam Finished", current_thread().name)