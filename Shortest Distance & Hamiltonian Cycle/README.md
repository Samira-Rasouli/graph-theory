**Code Explanation:**

**1. Hamiltonian Path Algorithm:**

The program attempts to find a Hamiltonian Path in a given graph, which is a path that visits each vertex exactly once. The path is then animated to visually show the traversal.

**Functions:**
is_valid(v, pos, path, graph): Checks if a node v can be added to the current path at position pos.
hamiltonian_util(graph, path, pos): Recursively tries to find a Hamiltonian path by backtracking.
hamiltonian_cycle(graph): Initiates the Hamiltonian path search and returns the path if one is found.

**2. Floyd-Warshall Algorithm:**

The Floyd-Warshall algorithm is used to calculate **the shortest paths** between all pairs of nodes. It works by updating the shortest path between two nodes by considering an intermediate node at each iteration.

**Functions:**

floyd_warshall(graph): Computes the shortest paths and the next_node matrix, which helps in reconstructing the shortest path.
reconstruct_path(start, end, next_node): Reconstructs the shortest path between two nodes using the next_node matrix.

**3. Graph Animation:**

The graph is visualized using matplotlib and networkx, where the nodes and edges are drawn, and the Hamiltonian cycle is animated.

**Functions:**
animate_hamiltonian(graph, path, dist_matrix, next_node): Creates an animation to visualize the Hamiltonian cycle. It shows the edges of the cycle in red as they are traversed.

**4. Interactive Shortest Path Finder:**
The program allows the user to input two nodes and find the shortest path between them, displaying the path and its distance.

**Function:**

show_shortest_path_between_nodes(graph, dist_matrix, next_node): Prompts the user to enter two nodes and then displays the shortest path between them using the Floyd-Warshall algorithm.

**Example of Usage:**
Hamiltonian Path Calculation: The program first attempts to find a Hamiltonian cycle in the graph. If found, it animates the cycle.

Shortest Path Between Two Nodes: After the graph is processed, the user can input two nodes to find the shortest path between them.

**Example Graph:**
The graph used in this program consists of 8 nodes, where an edge between two nodes is represented by a 1 in the adjacency matrix.

graph = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]


![hamiltonian_cycle](https://github.com/user-attachments/assets/45f1ed80-e58d-47aa-9903-e1a90b23b0e8)
