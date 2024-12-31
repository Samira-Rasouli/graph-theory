import networkx as nx
import matplotlib.pyplot as plt
import random
from collections import deque

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def generate_random_hypergraph():
    num_nodes = random.randint(5, 10)  # Random number of main nodes
    num_hyperedges = random.randint(3, 7)  # Random number of hyperedges

    nodes = list(range(1, num_nodes + 1))
    hyperedges = []

    for _ in range(num_hyperedges):
        # Create a random hyperedge with at least 2 and at most all nodes
        hyperedge = random.sample(nodes, random.randint(2, len(nodes)))
        hyperedges.append(hyperedge)

    return nodes, hyperedges

def main():
    # Generate random hypergraph
    nodes, hyperedges = generate_random_hypergraph()

    # Define the hypergraph (using a bipartite graph for modeling)
    H = nx.Graph()

    # Add edges to the bipartite graph
    for i, hyperedge in enumerate(hyperedges):
        hyperedge_node = f"h{i}"  # A special node for each hyperedge
        for node in hyperedge:
            H.add_edge(hyperedge_node, node)

    # Compute the degree of each node (only for main nodes)
    degrees = {node: H.degree(node) for node in H.nodes if not str(node).startswith('h')}

    # Print the degree of each node
    print("Degree of each node in the hypergraph:")
    for node, degree in degrees.items():
        print(f"Node {node}: Degree {degree}")

    # Perform DFS traversal starting from node 1 (if it exists)
    print("\nDFS Traversal starting from node 1:")
    if 1 in H:
        dfs(H, 1)
    else:
        print("Node 1 not found in the graph.")

    # Perform BFS traversal starting from node 1 (if it exists)
    print("\nBFS Traversal starting from node 1:")
    if 1 in H:
        bfs(H, 1)
    else:
        print("Node 1 not found in the graph.")

    # Draw the hypergraph with specific layout
    pos = nx.spring_layout(H)  # Determine positions for the nodes

    # Separate hyperedge nodes and main nodes
    hyperedge_nodes = [node for node in H.nodes if str(node).startswith('h')]
    main_nodes = [node for node in H.nodes if not str(node).startswith('h')]

    # Draw main nodes and hyperedge nodes separately
    nx.draw_networkx_nodes(H, pos, nodelist=main_nodes, node_color="lightblue", node_size=1000, label="Main Nodes")
    nx.draw_networkx_nodes(H, pos, nodelist=hyperedge_nodes, node_color="orange", node_size=800, label="Hyperedges")
    nx.draw_networkx_edges(H, pos, edge_color="gray")
    nx.draw_networkx_labels(H, pos, font_size=10)

    plt.legend()
    plt.title("Random Hypergraph")
    plt.show()

if __name__ == "__main__":
    main()
