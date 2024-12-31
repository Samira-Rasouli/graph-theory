# random_graph-Erdos-Renyi-model

**How the Code Works:**

**1. Generating a Random Graph:**
The function nx.erdos_renyi_graph is used to generate a random graph based on **the Erdős–Rényi model**.

The number of nodes is specified (num_nodes).

The probability of an edge between each pair of nodes is defined (prob_edge).


**2. Graph Analysis:**

The number of nodes and edges is printed.

It checks whether the graph is connected or not.

If the graph is not connected, the largest connected component is identified.


**3. Graph Visualization:**

The graph is visualized using matplotlib and functions from the networkx library.
