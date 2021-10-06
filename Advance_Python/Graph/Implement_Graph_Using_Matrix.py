# Python program to implement graph


nodes = []          # list of node
graph = []          # create graph
node_count = 0      # count the node


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


def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        graph[index2][index1] = cost


# delete a node
def delete_node(val):
    global node_count
    if val not in nodes:
        print(val, "is not present in the graph")
    else:
        index1 = nodes.index(val)
        node_count -= 1             # decrement the counter
        nodes.remove(val)           # remove the node from nodes list
        graph.pop(index1)           # pop the whole row
        for i in graph:
            i.pop(index1)


# delete a edge
def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)  # get the index of v1
        index2 = nodes.index(v2)  # get the index of v2

        graph[index1][index2] = 0
        graph[index2][index1] = 0


# print the graph in matrix form
def print_graph():
    for i in range(node_count):         # outer loop
        for j in range(node_count):     # inner loop
            print(format(graph[i][j], "<3"), end=" ")
        print()


# add node
add_node("A")
add_node("B")
add_node("C")

# add edge
add_edge("A", "B", 10)
add_edge("B", "C", 20)
add_edge("C", "D", 30)
print_graph()
print("Nodes : ", nodes)

# delete node
delete_node("D")
print("Graph after deletion")

# delete edge
delete_edge("A", "B")
print("nodes : ", nodes)

# display
# print(graph)          # display in list in list [nested list] form
print_graph()           # display in matrix form
