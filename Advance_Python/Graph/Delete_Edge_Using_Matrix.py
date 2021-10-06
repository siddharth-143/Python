# Python program to implement deletion operation | delete edge | using adjacency matrix

nodes = []
graph = []
count_node = 0


# delete edge for undirected graph and it also work for weighted and unweighted graph
def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)        # get the index of v1
        index2 = nodes.index(v2)        # get the index of v2

        graph[index1][index2] = 0
        graph[index2][index1] = 0


# delete edge for directed graph weighted and unweighted graph
def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in the graph")
    elif v2 not in nodes:
        print(v2, "is not present in the graph")
    else:
        index1 = nodes.index(v1)        # get the index of v1
        index2 = nodes.index(v2)        # get the index of v2

        graph[index1][index2] = 0
        # graph[index2][index1] = 0


delete_edge("A", "B")
