# Python program to implement DFS using recursion

def add_node(val):
    if val in graph:
        print(val, "is already present in the graph")
    else:
        graph[val] = []


def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the graph")
    elif v2 not in graph:
        print(v1, "is not present in the graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

def DFS(node, visited, graph):
    if node not in graph:
        print(node, "Node is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)


visited = set()
graph = {}

add_node("A")
add_node("B")
add_node("C")
add_node("D")

add_edge("A", "B")
add_edge("A", "C")
add_edge("A", "D")
print(graph)

DFS("K", visited, graph)