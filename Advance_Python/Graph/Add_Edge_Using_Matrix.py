# Python program to implement graph insertion operation | add edge | adjacency matrix

# add edge for undirected graph
def add_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)            # get the index of v1
        index2 = nodes.index(v2)            # get the index of v2
        graph[index1][index2] = 1
        graph[index2][index1] = 1


# add edge for undirected weighted graph
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


# add edge to directed graph with weighted
def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = cost
        # graph[index2][index1] = cost

# add edge to directed without weight
def add_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1


nodes = []
graph = []
add_edge("A", "B")
add_edge("A", "B", 10)
add_edge("B", "C", 20)
add_edge("D", "E")