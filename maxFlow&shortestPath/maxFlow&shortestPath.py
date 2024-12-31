import networkx as nx
import random

# Create a random graph
def create_random_graph(num_nodes):
    edge_probability = min(0.4, 1 / num_nodes)  # Dynamic probability based on the number of nodes
    G = nx.DiGraph()  # Directed graph for flow calculation
    G.add_nodes_from(range(num_nodes))
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < edge_probability:
                capacity = random.randint(1, 10)  # Random edge capacities
                G.add_edge(i, j, capacity=capacity)
    return G

# Display shortest paths between all pairs of nodes
def shortest_paths(graph):
    paths = dict(nx.all_pairs_dijkstra_path(graph))
    lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    print("Shortest paths and their lengths:")
    for source in paths:
        for target in paths[source]:
            print(f"Shortest path from {source} to {target}: {paths[source][target]}, Length: {lengths[source][target]}")
    print("\n")

# Calculate the maximum flow between two nodes
def max_flow(graph, source, target):
    flow_value, flow_dict = nx.maximum_flow(graph, source, target, capacity='capacity')
    print(f"Maximum flow from {source} to {target}: {flow_value}")
    print("Flow distribution:")
    for u, flows in flow_dict.items():
        for v, flow in flows.items():
            if flow > 0:
                print(f"  {u} -> {v}: {flow}")
    print("\n")

# Predict the existence of an edge between two nodes
def predict_edge(graph, node1, node2):
    # Use Jaccard coefficient as a simple similarity measure
    preds = nx.jaccard_coefficient(graph.to_undirected(), [(node1, node2)])
    for u, v, p in preds:
        print(f"Predicted probability of edge between {u} and {v}: {p:.2f}")
    return p

# Graph configuration
num_nodes = 10  # Number of nodes

# Generate the graph and calculate shortest paths and maximum flow
G = create_random_graph(num_nodes)
shortest_paths(G)

# Select two random nodes for maximum flow calculation
source = random.randint(0, num_nodes - 1)
target = random.randint(0, num_nodes - 1)
while source == target:  # Ensure source and target are different
    target = random.randint(0, num_nodes - 1)

max_flow(G, source, target)

# Predict the existence of an edge between two random nodes
node1 = random.randint(0, num_nodes - 1)
node2 = random.randint(0, num_nodes - 1)
while node1 == node2 or G.has_edge(node1, node2):  # Ensure no direct edge exists
    node2 = random.randint(0, num_nodes - 1)

print(f"Predicting edge existence between nodes {node1} and {node2}:")
predict_edge(G, node1, node2)

# Draw the graph
import matplotlib.pyplot as plt
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['capacity'] for u, v, d in G.edges(data=True)})
plt.show()
