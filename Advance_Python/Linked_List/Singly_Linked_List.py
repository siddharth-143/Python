# Python program to implement singly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beg(self):  # insert element at beginning
        data = int(input("Enter a data at beginning : "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self):        # insert at end
        data = int(input("Enter a data at end : "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):          # display the list
        if self.head is None:
            print("Linked list is empty!")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next


l = Linked_List()
l.insert_at_beg()
l.insert_at_end()
l.display()
