
from collections import deque

graph = {
    'A': ['A', 'B'],
    'C': ['A', 'E', 'D'],
    'B': ['A'],
    'E': ['C'],
    'D': ['C']
}

def bfs_all_nodes(graph):
    visited = set()
    
   
    for start_node in graph:
        
        if start_node not in visited:
            queue = deque([start_node])
            
            while queue:
                node = queue.popleft()
                if node not in visited:
                    print(node, end=" ")
                    visited.add(node)
                    
                    for neighbour in graph[node]:
                        if neighbour not in visited:
                            queue.append(neighbour)

print("BFS Traversal of all nodes:")
bfs_all_nodes(graph)

