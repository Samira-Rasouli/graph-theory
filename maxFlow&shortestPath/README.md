**Random Graph Analysis: Shortest Paths, Maximum Flow, and Edge Prediction**

Overview
This Python script creates a directed random graph using networkx, calculates shortest paths, computes maximum flow between nodes, and predicts the existence of edges between nodes using the Jaccard coefficient. The script also visualizes the graph with node labels, edge capacities, and flow information.

**Features**

**Random Graph Generation:**

Creates a directed graph (DiGraph) with n nodes.
Adds edges probabilistically using a dynamic edge probability based on the number of nodes.
**Shortest Paths Calculation:**

Computes and displays the shortest paths and their lengths between all pairs of nodes using Dijkstra's algorithm.
**Maximum Flow Calculation:**

Selects random source and target nodes and calculates the maximum flow using the Edmonds-Karp algorithm.
Displays the flow distribution for each edge in the flow network.
**Edge Existence Prediction:**

Uses the Jaccard coefficient to predict the probability of an edge between two given nodes.
**Graph Visualization:**

Visualizes the graph using matplotlib with nodes, edges, and edge capacities.
**Code Explanation**

**1. Random Graph Creation**

def create_random_graph(num_nodes):
    edge_probability = min(0.3, 1 / num_nodes)  # Dynamic probability based on the number of nodes
    G = nx.DiGraph()  # Directed graph for flow calculation
    G.add_nodes_from(range(num_nodes))  # Add nodes to the graph
    for i in range(num_nodes):
        for j in range(num_nodes):
            # Ensure no self-loops and decide edge existence based on edge_probability
            if i != j and random.random() < edge_probability:
                capacity = random.randint(1, 10)  # Assign random capacities to edges
                G.add_edge(i, j, capacity=capacity)
    return G
Nodes are added from 0 to num_nodes - 1.
Edges are created with a random probability that ensures the graph remains sparse for large num_nodes.
Each edge is assigned a random capacity between 1 and 10.

**2. Shortest Paths**

def shortest_paths(graph):
    paths = dict(nx.all_pairs_dijkstra_path(graph))
    lengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    print("Shortest paths and their lengths:")
    for source in paths:
        for target in paths[source]:
            print(f"Shortest path from {source} to {target}: {paths[source][target]}, Length: {lengths[source][target]}")
    print("\n")
Uses Dijkstra's algorithm to calculate the shortest paths and their lengths.
Displays the results for all source-target pairs.

**3. Maximum Flow**

def max_flow(graph, source, target):
    flow_value, flow_dict = nx.maximum_flow(graph, source, target, capacity='capacity')
    print(f"Maximum flow from {source} to {target}: {flow_value}")
    print("Flow distribution:")
    for u, flows in flow_dict.items():
        for v, flow in flows.items():
            if flow > 0:
                print(f"  {u} -> {v}: {flow}")
    print("\n")
Calculates the maximum flow between a source and target node using the networkx implementation of the Edmonds-Karp algorithm.
Displays the flow value and distribution for each edge.

**4. Edge Prediction**

def predict_edge(graph, node1, node2):
    preds = nx.jaccard_coefficient(graph.to_undirected(), [(node1, node2)])
    for u, v, p in preds:
        print(f"Predicted probability of edge between {u} and {v}: {p:.2f}")
    return p
Uses the Jaccard coefficient to predict the likelihood of an edge between two nodes.
Only evaluates for nodes without an existing edge between them.

**Usage**
The script generates a graph with 10 nodes by default. Adjust num_nodes to experiment with graphs of different sizes.
Edge probabilities are dynamically adjusted to maintain sparse graphs for large numbers of nodes.
Run the script to view the shortest paths, maximum flow, edge predictions, and graph visualization.

**Example Output**
**Graph Details:**

Shortest path from 2 to 9: [2, 5, 7, 1, 9], Length: 4

Maximum flow from 6 to 9: 1

Predicted probability of edge between 5 and 8: 0.17

**Visualization:**

Nodes and edges are drawn with capacities displayed.

![image](https://github.com/user-attachments/assets/206964f7-c6c9-4003-b553-a0479792193f)

