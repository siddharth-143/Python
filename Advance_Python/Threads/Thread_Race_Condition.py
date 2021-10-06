# Thread Race Condition

from threading import Thread, current_thread

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat

    def reserve(self, need_seat):
        print("Available Seats : ", self.available_seat)

        if(self.available_seat >= need_seat):
            name = current_thread().name
            print(f'{need_seat} seat is allocated for {name}')
            self.available_seat -= need_seat

        else:
            print("Sorry! All seats has allocated")

f = Flight(1)

t1 = Thread(target=f.reserve, args=(1,), name="Rahul")
t2 = Thread(target=f.reserve, args=(1,), name="Sonam")

t1.start()
t2.start()