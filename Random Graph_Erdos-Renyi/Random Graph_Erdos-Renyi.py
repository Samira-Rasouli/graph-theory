import networkx as nx
import matplotlib.pyplot as plt

# Parameters
num_nodes = 10   # Number of nodes
prob_edge = 0.4  # Probability of edge creation

# Generate a random graph using Erdős–Rényi model
random_graph = nx.erdos_renyi_graph(num_nodes, prob_edge)

# Print basic information about the graph
print("Number of nodes:", random_graph.number_of_nodes())
print("Number of edges:", random_graph.number_of_edges())

# Check if the graph is connected
is_connected = nx.is_connected(random_graph)
print("Is the graph connected?", is_connected)

# Find the largest connected component if the graph is not connected
if not is_connected:
    largest_cc = max(nx.connected_components(random_graph), key=len)
    print("Size of the largest connected component:", len(largest_cc))

# Plot the graph
pos = nx.spring_layout(random_graph)  # Node positions for visualization
plt.figure(figsize=(8, 6))
nx.draw(random_graph, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=500, font_size=10)
plt.title("Random Graph (Erdős–Rényi Model)")
plt.show()
