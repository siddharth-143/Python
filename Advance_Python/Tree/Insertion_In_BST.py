# Insertion in BST

class BST:
    def __init__(self, key=None):           # key=None   otherwise root=BST(None)
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:        # check node is empty or not
            self.key = data
            return
        if self.key == data:        # check for duplicate value and ignore it
            return
        if self.key > data:         # of data is less than root node
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)

    def search(self, data):
        if self.key == data:            # compare with root
            print(f"{data} Node is found!")
            return
        if data < self.key:         # compare with left
            if self.left:
                self.left.search(data)
            else:
                print(f"{data} Node is not present in tree")

        else:           # compare with right
            if self.right:
                self.right.search(data)
            else:
                print(f"{data} Node is not present in tree")

    def pre_order(self):            # pre order traversal
        print(self.key, end=" ")
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):         # in order traversal
        if self.left:
            self.left.in_order()
        print(self.key, end=" ")
        if self.right:
            self.right.in_order()

    def post_order(self):            # post order traversal
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.key, end=" ")

    def delete(self, data):             # delete node
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:
            if self.left:
                self.left = self.left.delete(data)
            else:
                print("Given node is not present in the tree")
        elif data > self.key:
            if self.right:
                self.right = self.right.delete(data)
            else:
                print("Given node is not present in the tree")
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            if self.right is None:
                temp = self.left
                self = None
                return temp
            node = self.right
            while node.left:
                node = node.left
            self.key = node.key
            self.right = self.right.delete(node.key)
        return self

    def min_node(self):         # minimum node of the tree
        current = self
        while current.left:
            current = current.left
        print("Node with smallest key is : ", current.key)

    def max_node(self):         # maximum node of tree
        current = self
        while current.right:
            current = current.right
        print("Node with largest key is : ", current.key)


root = BST()            # object
res = []
n = int(input("Enter a range of BST tree : "))
for i in range(n):
    val = int(input("Enter the elements of a BST tree : "))
    res.append(val)
    root.insert(val)
print(res)

# sear = int(input("Enter a element to search : "))           # search element
# root.search(sear)
#
# print("Pre order : ")
# pre = root.pre_order()          # pre order
# print(pre)
#
# print("In order : ")
# inor = root.in_order()
# print(inor)
#
# print("Post order : ")
# post = root.post_order()
# print(post)

# num = int(input("Enter a element to delete : "))
# print(root.delete(num))
# print(res)

root.min_node()         # minimum node
root.max_node()         # maximum node
