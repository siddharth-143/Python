# Python program to implement graph deletion operation | delete edge | using dictionary

nodes = []
graph = {}


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


# delete edge undirected and weighted graph
def delete_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        temp = [v1, cost]
        temp1 = [v2, cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)             # temp1 = v2
            graph[v2].remove(temp)              # temp = v1


# delete edge directed and unweighted graph
def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            # graph[v2].remove(v1)


# delete edge directed and weighted graph
def delete_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        temp = [v1, cost]
        temp1 = [v2, cost]
        if temp1 in graph[v1]:
            graph[v1].remove(temp1)             # temp1 = v2
            # graph[v2].remove(temp)              # temp = v1

