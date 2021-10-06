# Set & Get Thread

from threading import Thread, current_thread

# def disp():
#     print("Default Child Name : ", current_thread().name)
#     current_thread().name = "Flying Thread"
#     print("New Thread Name : ", current_thread().name)
#
# t = Thread(target=disp)
# t.start()
#
# print("Default Main Name : ", current_thread().name)
# current_thread().name = "Siddhu Thread"
# print("New Main Name : ", current_thread().name)

def disp():
    pass

t = Thread(target=disp)
print("Default : ", t.getName())        # getName
t.setName("Flying Thread")          # setName
print("New : ", t.getName())

print("Default name : ", t.name)     # name
t.name = "Python Thread"
print("New Name Thread", t.name)