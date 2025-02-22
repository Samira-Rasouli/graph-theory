# Tabu Search for Maximal Matching in a Graph

**Purpose of the Code**

This code implements the Tabu Search algorithm to find a **maximal matching** in a **randomly generated graph**. Finally, it visualizes the graph with the matching edges highlighted in red.

**Code Sections and Their Functions**

**1. Generating a Random Graph**


    def generate_graph(n, p):

    """Generate a random graph with n nodes and probability p for each edge."""

    G = nx.erdos_renyi_graph(n, p)

    return G

Generates a **random graph** using the **Erdős–Rényi** model, where each edge is added with probability p.

**2. Checking if a Set of Edges Forms a Matching**


    def is_matching(M, G):

    """Check if the set of edges forms a valid matching."""
    
    nodes = set()
    for u, v in M:
        if u in nodes or v in nodes:
            return False
        nodes.add(u)
        nodes.add(v)
    return True

Ensures that the set of edges M forms a valid matching.

In a matching, no vertex should appear in more than one edge.

**3. Constructing a Maximal Matching Using a Greedy Approach**

    def maximal_matching(G):

    """Generate a maximal matching greedily."""
    M = set()
    nodes = set()
    for u, v in G.edges():
        if u not in nodes and v not in nodes:
            M.add((u, v))
            nodes.add(u)
            nodes.add(v)
    return M

Creates a maximal matching (not necessarily maximum).

Iterates through edges and adds only those that do not share vertices with existing edges.

**4. Generating Neighboring Matchings for Tabu Search**


    def create_neighbors(M, G):

    """Create neighbors by adding new edges and removing conflicting ones."""
    
    neighbors = []
    edges = list(G.edges())
    new_M = M.copy()
    for e in edges:
        if e not in M:
            new_M.add(e)
            for u, v in list(new_M):
                if u in e or v in e:
                    new_M.discard((u, v))
            if is_matching(new_M, G):
                neighbors.append(new_M)
    return neighbors
    
Generates new neighboring solutions by adding a new edge and removing conflicting edges.

If the modified set still forms a valid matching, it is added to the list of neighbors.

**5. Implementing the Tabu Search Algorithm**


    def tabu_search(G, max_iter=10, tabu_size=3):
    """Run the Tabu Search algorithm to find the best maximal matching."""
    current_M = maximal_matching(G)
    best_M = current_M
    tabu_list = []

    for _ in range(max_iter):
        neighbors = create_neighbors(current_M, G)
        if not neighbors:
            break

        # Select the best neighbor that is not in the tabu list
        best_neighbor = max(neighbors, key=len, default=current_M)
        if best_neighbor in tabu_list:
            continue

        current_M = best_neighbor
        if len(current_M) > len(best_M):
            best_M = current_M

        tabu_list.append(best_neighbor)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)

    return best_M
    
Executes Tabu Search to find a better maximal matching.

In each iteration, selects the best neighbor that is not in the tabu list.

If the new matching is better, it becomes the best found solution.

The tabu list prevents revisiting previous solutions, maintaining a history of the last three steps.

**6. Visualizing the Graph and the Found Matching**


    def draw_graph(G, matching):

    """Visualize the graph with matching edges highlighted in red."""
    
    pos = nx.spring_layout(G)
    plt.figure(figsize=(6, 6))
    nx.draw(G, pos, with_labels=True, edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=matching, edge_color='red', width=2)
    plt.show()
    
Draws the graph and highlights the edges belonging to the maximal matching in red.

**7. Running the Program**


  graph = generate_graph(10, 0.3)

  max_matching = tabu_search(graph)

  draw_graph(graph, max_matching)

  Generates a random graph with 10 nodes and 0.3 probability for each edge.

Executes Tabu Search to find a maximal matching.

Visualizes the graph with the found matching.
