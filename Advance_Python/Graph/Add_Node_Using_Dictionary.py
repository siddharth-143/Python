# Python program to implement graph insertion operation | add node | using dictionary

graph = {}


def add_node(val):
    if val in graph:
        print(val, "is already present in the graph")
    else:
        graph[val] = []


add_node("A")
add_node("B")
print(graph)