# Python program to implement graph insertion operation | add edge | using dictionary

# undirected graph
def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)


# undirected weighted graph
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        list1 = [v2, cost]
        list2 = [v1, cost]
        graph[v1].append(list1)
        graph[v2].append(list2)


# directed graph
def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        graph[v1].append(v2)
        # graph[v2].append(v1)


# directed weighted graph
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        list1 = [v2, cost]
        # list2 = [v1, cost]
        graph[v1].append(list1)
        # graph[v2].append(list1)


graph = {}
add_edge("A", "B")
add_edge("A", "B", 10)
print(graph)