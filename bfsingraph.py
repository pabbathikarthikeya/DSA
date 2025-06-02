from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs_in_graph(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        value=queue.popleft()
        if value not in visited:
            print(value,end=" ")
            visited.add(value)
            for neighbor in graph[value]:
                queue.append(neighbor)
print("BFS traversal in graph:")
bfs_in_graph(graph,'A')
