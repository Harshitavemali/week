def dfs(graph, startnode):
    visitednode = set()
    stack = [startnode]
    while stack:
        currentnode = stack.pop()
        if currentnode not in visitednode:
            print(currentnode, end=" -> ")
            visitednode.add(currentnode)
            for neighbor in reversed(graph[currentnode]):
                if neighbor not in visitednode:
                    stack.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


dfs(graph, 'A')
