"""
    Python program to create a linked list and display the elements in the list
"""

class Node:
    def __init__(self, data):
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

a_llist = Linked_List()
n = int(input("How many elements would you like to add : "))
for i in range(n):
    data = int(input("Enter data item : "))
    a_llist.append(data)
print("The lined list : ", end=" ")
a_llist.display()