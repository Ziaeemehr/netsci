import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def plot_graph(G, **kwargs):
    """
    Plots a NetworkX graph with customizable options.

    Parameters:
    - G: A NetworkX graph object (nx.Graph, nx.DiGraph, etc.).
    - kwargs: Additional keyword arguments to customize the plot. These can include:
      - 'node_color': Color of the nodes (can be a single color or a list of colors).
      - 'node_size': Size of the nodes (single value or list of sizes).
      - 'edge_color': Color of the edges (can be a single color or a list of colors).
      - 'width': Width of the edges.
      - 'with_labels': Whether to draw node labels or not.
      - 'font_size': Size of the font for node labels.
      - 'font_color': Color of the font for node labels.
      - 'title': Title of the plot.
      - 'seed': Seed for the random layout algorithm (optional).
      - 'figsize': Size of the figure (optional).
    """

    # Extracting optional arguments
    node_color = kwargs.get("node_color", "lightblue")
    node_size = kwargs.get("node_size", 300)
    edge_color = kwargs.get("edge_color", "black")
    width = kwargs.get("width", 1.0)
    with_labels = kwargs.get("with_labels", True)
    font_size = kwargs.get("font_size", 12)
    font_color = kwargs.get("font_color", "black")
    title = kwargs.get("title", None)
    seed = kwargs.get("seed", None)
    edge_labels = kwargs.get("edge_labels", None)
    figsize = kwargs.get("figsize", (4, 4))
    
    if "figsize" in kwargs:
        plt.figure(figsize=figsize)
        plt.axis("off")

    if seed is not None:
        np.random.seed(seed)  # Set the random seed for reproducibility

    # Position nodes using a layout algorithm
    pos = nx.spring_layout(
        G, seed=seed
    )  # You can choose other layouts like nx.circular_layout(G) or nx.kamada_kaway_layout(G)

    # Draw the network
    nx.draw(
        G,
        pos,
        node_color=node_color,
        node_size=node_size,
        edge_color=edge_color,
        width=width,
        with_labels=with_labels,
        font_size=font_size,
        font_color=font_color,
    )

    if edge_labels is not None:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Set the plot title
    if title is not None:
        plt.title(title)

    # Show the plot
    # plt.show()


def find_sap(graph, start, target, path=None):
    """
    This function finds all self-avoiding paths (SAPs) in a given graph from a start node to a target node.
    A self-avoiding path is a path that does not revisit any node.

    Parameters:
    - graph (NetworkX graph): The input graph where SAPs will be found.
    - start (str or int): The node where the search for SAPs starts.
    - target (str or int): The node where the search for SAPs ends.
    - path (list, optional): Internal parameter used to keep track of the current path during the search.

    Yields:
    - list: A self-avoiding path from the start node to the target node.

    Example usage:
    >>> G = nx.Graph()
    >>> edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')]
    >>> G.add_edges_from(edges)
    >>> start_node = 'A'
    >>> target_node = 'F'
    >>> all_saps = list(find_sap(G, start_node, target_node))
    >>> for path in all_saps:
    >>>     print("->".join(path))
    """
    if path is None:
        path = []

    path.append(start)
    
    if start == target:
        yield path[:]
    else:
        for neighbor in graph.neighbors(start):
            if neighbor not in path:
                yield from find_sap(graph, neighbor, target, path)
    
    path.pop()
    
    
def is_hamiltonian_path(G, path):
    return all(G.has_edge(path[i], path[i + 1]) for i in range(len(path) - 1))

def find_hamiltonian_path(G):
    nodes = list(G.nodes())
    for perm in itertools.permutations(nodes):
        if is_hamiltonian_path(G, perm):
            return perm
    return None


# Example usage:
if __name__ == "__main__":
    G = nx.erdos_renyi_graph(10, 0.3)
    plot_graph(
        G,
        node_color="skyblue",
        node_size=500,
        edge_color="gray",
        width=2,
        title="Sample NetworkX Graph",
    )
    plt.show()
