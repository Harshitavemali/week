graph = {}


n = int(input("Enter the number of nodes: "))


for i in range(n):
    ver = input("Enter the vertex: ")
    neigh = input("Enter the neighboring nodes (comma-separated): ").split(',')
    graph[ver] = neigh


startnode = input("Enter the start node: ")


if startnode in graph:
    print(f"Neighbors of {startnode}: {graph[startnode]}")
else:
    print(f"{startnode} is not present in the graph")
