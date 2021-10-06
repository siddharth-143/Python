# Python program to implement graph insertion operaton | add node | adjacency matrix

def add_node(val):
    global node_count
    if val in nodes :
        print(val, "is already present in the graph!")
    else:
        node_count += 1
        nodes.append(val)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)


# print the tree in matrix form
def print_graph():
    for i in range(node_count):         # outer loop
        for j in range(node_count):     # inner loop
            print(format(graph[i][j], "<3"), end=" ")
        print()


nodes = []          # list of node
graph = []          # create graph
node_count = 0      # count the node

add_node("A")
add_node("B")
add_node("C")
print(graph)
print_graph()
