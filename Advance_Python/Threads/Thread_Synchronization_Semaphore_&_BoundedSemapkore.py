# Thread Synchronization Semaphore and BoundedSemaphore

from threading import *

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.l = Semaphore(2)           # self.l = BoundedSemaphore
        print("Semaphore Before: ", self.l)

    def reserve(self, need_seat):
        print("Available Seat : ", self.available_seat)

        self.l.acquire()
        self.l.acquire()
        print("Semaphore After : ", self.l)

        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f"{need_seat} seat is allocated for {name}")
            self.available_seat -= need_seat

        else:
            print("Sorry! All seats has allocated")
        self.l.release()
        self.l.release()


f = Flight(2)

t1 = Thread(target=f.reserve, args=(1,), name="Rahul")
t2 = Thread(target=f.reserve, args=(1,), name="Sonam")
t3 = Thread(target=f.reserve, args=(1,), name="Karan")

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("Main Thread")