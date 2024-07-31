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
