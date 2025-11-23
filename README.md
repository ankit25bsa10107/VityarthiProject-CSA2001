# VityarthiProject-CSA2001


# --Project : BFS AIML PROJECT VITYARTHI--

# DESCRIPTION
This project demonstrates the working of the Breadth-First Search (BFS) algorithm using a graph represented with an adjacency list. The graph contains two separate connected components. When BFS is applied starting from node A, it explores nodes level-by-level and visits only the nodes that are reachable from the starting point. In this case, BFS visits A and B, showing how the algorithm handles self-loops, directed edges, and disconnected parts of a graph.The project helps in understanding how BFS works internally, how graphs are traversed, and how reachability is determined in networks, social connections, and real-life systems.

# Algorithm:
1. Start
2. Define the graph as an adjacency list with nodes A, B, C, D, and E.
3. Create an empty set visited to keep track of visited nodes.
4. Initialize a queue and insert the starting node (A) into it.
5. Repeat until the queue becomes empty:
-	Remove the first node from the queue → call it node.
-	If node is not in visited:
               1. Print/visit the node.
               2. Add the node to visited.
               3. For each neighbour of the node in the graph:
-	If the neighbour is not visited, add it to the queue.
6. End the loop when no more nodes are left to explore.
7. Stop.
 	
# FEATURES
1. Uses an adjacency list to represent the graph.
2. Uses a queue (deque) for BFS traversal.
3. Handles self-loops and directed edges.
4. Visits only reachable nodes from the start node.
5. Uses a visited set to avoid repetition.
6. Simple, clear, and beginner-friendly implementation.
   
# TECHNOLOGY
1.	Git and GitHub (Version Control)
2.	Python (Programming language used)
3.	VS Code (Code Editor)

# MADE BY
  Ankit Kumar




