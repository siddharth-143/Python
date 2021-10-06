"""
    Python program to read linked list in reverse order
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

a_llist = Linked_List()
n = int(input("How many elements you would you like to add : "))
for i in range(n):
    data = int(input("Enter data items : "))
    node = Node(data)
    a_llist.insert_at_beg(node)

print("The Linked List : ", end=" ")
a_llist.display()
