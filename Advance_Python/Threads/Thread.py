# Thread

from threading import Thread

def disp(a, b):
    for i in range(5):
        print("Child Thread")
        print(a,b)

t = Thread(target=disp, args=(10, 20))

t.start()

for i in range(5):
    print("Main Thread")