# Python program to implement queue using list

queue = []

def enqueue():
    ele = int(input("Enter the element : "))
    queue.append(ele)
    print(queue)

def dequeue():
    if not queue:
        print("Queue is Empty!")
    else:
        e = queue.pop(0)
        print("Removed Element : ", e)
        print(queue)

def display():
    print(queue)

while True:

    print("1. Push \n2. Pop \n3. Display \n4. Exit")
    n = int(input("Enter your choice : "))

    if n == 1:
        enqueue()
    elif n == 2:
        dequeue()
    elif n == 3:
        display()
    elif n == 4:
        break
    else:
        print('Enter a right choice!')