"""
    Python program to search for an element in the linked list without using recursion
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next

    def find_index(self, key):
        current = self.head

        index = 0
        while current:
            if current.data == key:
                return index
            current = current.next
            index = index + 1
        return -1

a_list = Linked_List()
n = int(input("How many element you would you like to add : "))
for i in range(n):
    data = int(input("Enter data item : "))
    a_list.append(data)

print("The Linked list : ", end=" ")
a_list.display()
print()

key = int(input("What data would you like to search for : "))
index = a_list.find_index(key)
if index == -1:
    print(str(key) + " was not found")
else:
    print(str(key) + " is at index " + str(index))