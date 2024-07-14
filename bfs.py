from queue import Queue
def bfs(graph, startnode):
    visitednode = set()
    queue = Queue()
    queue.put(startnode)
    visitednode.add(startnode)
    
    while not queue.empty():
        currentnode = queue.get()
        print(currentnode, end=" -> ")
        
        for neighbor in graph[currentnode]:
            if neighbor not in visitednode:
                queue.put(neighbor)
                visitednode.add(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
bfs(graph, 'A')
