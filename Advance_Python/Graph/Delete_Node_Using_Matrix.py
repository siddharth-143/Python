# Python Program to implement graph deletion operation | delete node | using adjacency matrix

nodes = []
graph = []
count_node = 0


# delete the node
def delete_node(val):
    global count_node
    if val not in nodes:
        print(val, "is not present in the graph")
    else:
        index1 = nodes.index(val)
        count_node -= 1             # decrement the counter
        nodes.remove(val)           # remove the node from nodes list
        graph.pop(index1)           # pop the whole row
        for i in graph:
            i.pop(index1)


delete_node("A")