# Python program to implement graph deletion operation | delete node | using dictionary

nodes = []
graph = {}

# delete a node undirected and unweighted
def delete_node(val):
    if val not in graph:
        print(val, "is not present in the graph")
    else:
        graph.pop(val)          # pop the key with all values
        for i in graph:         # traverse the dictionary
            list1 = graph[i]            # assign values to list
            if val in list1:
                return list1.remove(val)            # remove the value


# delete a node directed and wighted graph
def delete_node(val):
    if val not in graph:
        print(val, "is not present in the graph")
    else:
        graph.pop(val)          # pop the key with all values
        for i in graph:         # traverse the dictionary
            list1 = graph[i]            # assign values to list
            for j in list1:             # search for the value in list1 nested list
                if val == j[0]:          # check first index of the value
                    list1.remove(j)
                    break


delete_node("A")
delete_node("B")