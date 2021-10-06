# Python program to implement graph using dictionary

# add node
def add_node(val):
    if val in graph:
        print(val, "is already present in the graph")
    else:
        graph[val] = []


# add edge
def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

# delete node
def delete_node(val):
    if val not in graph:
        print(val, "is not present in the graph")
    else:
        graph.pop(val)          # pop the key with all values
        for i in graph:         # traverse the dictionary
            list1 = graph[i]            # assign values to list
            if val in list1:
                return list1.remove(val)            # remove the value


# delete edge undirected and unweighted graph
def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)


# graph
graph = {}

# add node
add_node("A")
add_node("B")
add_node("C")

# add edge
add_edge("A", "B")
add_edge("B", "C")
print(graph)

# delete node
# delete_node("A")
print("After deleting : ")

# delete edge
delete_edge("B", "C")

# display
print(graph)
