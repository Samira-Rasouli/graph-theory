import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def is_valid(v, pos, path, graph):
    if graph[path[pos - 1]][v] == 0:
        return False
    if v in path:
        return False
    return True


def hamiltonian_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        return False

    for v in range(1, len(graph)):
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamiltonian_util(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False


def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0
    if not hamiltonian_util(graph, path, 1):
        return None
    return path


# Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices
def floyd_warshall(graph):
    n = len(graph)
    dist = np.full((n, n), np.inf)
    next_node = np.full((n, n), -1)

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                dist[i][j] = 1
                next_node[i][j] = j
            if i == j:
                dist[i][j] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node


# Function to reconstruct the path from the next_node matrix
def reconstruct_path(start, end, next_node):
    path = []
    if next_node[start][end] == -1:
        return path  # if no path exists
    while start != end:
        path.append(start)
        start = next_node[start][end]
    path.append(end)
    return path


def animate_hamiltonian(graph, path, dist_matrix, next_node):
    G = nx.Graph()
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12, ax=ax)

    if not path:
        plt.title("No Hamiltonian Path found", fontsize=16)
        plt.show()
        return

    edge_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)] + [(path[-1], path[0])]
    edge_colors = ['red'] * len(edge_path)
    drawn_edges = []

    def update(frame):
        if frame < len(edge_path):
            drawn_edges.append(edge_path[frame])
            nx.draw_networkx_edges(G, pos, edgelist=drawn_edges, edge_color=edge_colors[:len(drawn_edges)], ax=ax,
                                   width=2)
        elif frame == len(edge_path):
            plt.title("Hamiltonian Cycle Complete!", fontsize=16)

    ani = FuncAnimation(fig, update, frames=len(edge_path) + 1, interval=1000, repeat=False)
    plt.show()


# New function to receive user input and show the shortest path between two nodes
def show_shortest_path_between_nodes(graph, dist_matrix, next_node):
    print("Enter two nodes (0 to", len(graph) - 1, ") to find the shortest path between them:")
    start = int(input("Enter start node: "))
    end = int(input("Enter end node: "))

    if start < 0 or end < 0 or start >= len(graph) or end >= len(graph):
        print("Invalid nodes! Please enter valid node indices.")
        return

    # Reconstruct the shortest path
    path = reconstruct_path(start, end, next_node)
    if path:
        print(f"Shortest path from node {start} to node {end} is {dist_matrix[start][end]} with path: {path}")
    else:
        print(f"No path exists between node {start} and node {end}.")


# Example graph with 8 nodes
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

path = hamiltonian_cycle(graph)

if path:
    print("Hamiltonian Path:", path)
    dist_matrix, next_node = floyd_warshall(graph)  # Calculate the shortest paths
    animate_hamiltonian(graph, path, dist_matrix, next_node)  # Show Hamiltonian path animation
else:
    print("No Hamiltonian Path found")
    dist_matrix, next_node = floyd_warshall(graph)
    animate_hamiltonian(graph, None, dist_matrix, next_node)  # Show animation without Hamiltonian path

# Show shortest path between two nodes
show_shortest_path_between_nodes(graph, dist_matrix, next_node)
