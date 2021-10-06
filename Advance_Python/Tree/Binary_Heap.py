# Python program to implement binary heap

class Binary_Heap:
    def __init__(self):
        self.item = []

    def size(self):         # size of heap
        return len(self.item)

    def parent(self, i):            # parent node of heap
        return (i - 1)//2

    def left(self, i):          # left child of heap
        return 2*i + 1

    def right(self, i):         # right child of heap
        return 2*i + 2

    def get(self, i):           # current node of heap
        return self.item[i]

    def get_max(self):          # max node of heap
        if self.size() == 0:
            return
        return self.item[0]

    def extract_max(self):          # delete a node
        if self.size() == 0:
            return
        largest = self.get_max()
        self.item[0] = self.item[-1]
        del self.item[-1]
        self.max_heapify(0)
        return largest

    def max_heapify(self, i):           # max heapify algorithm
        l = self.left(i)
        r = self.right(i)
        if l <= self.size() - 1 and self.get(l) > self.get(i):
            largest = l
        else:
            largest = i
        if r <= self.size() - 1 and self.get(r) > self.get(largest):
            largest = r
        if largest != i:
            self.swap(largest, i)
            self.max_heapify(largest)

    def swap(self, i, j):           # swaping
        self.item[i], self.item[j] = self.item[j], self.item[i]

    def insert(self):           # inset a node in heap
        key = int(input("Enter a element : "))
        index = self.size()
        self.item.append(key)

        while index != 0:
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
                index = p

bheap = Binary_Heap()

print("1. Insert \n2. Max Get \n3. Max Extract \n4. Exit")

while True:
    n = int(input("Enter your choice : "))
    if n == 1:
        bheap.insert()
    elif n == 2:
        print("Max value : ", bheap.get_max())
    elif n == 3:
        print("Max value removed : ", bheap.extract_max())
    elif n == 4:
        break
    else:
        print("Enter a right choice!")