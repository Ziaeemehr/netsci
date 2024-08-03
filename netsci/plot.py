import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



def plot_graph(G, **kwargs):
    """
    Plots a NetworkX graph with customizable options.

    Parameters
    ----------
    G : NetworkX graph
        A NetworkX graph object (e.g., nx.Graph, nx.DiGraph).
    **kwargs : keyword arguments
        Additional keyword arguments to customize the plot. These can include:
        
        node_color : str or list, optional
            Color of the nodes (can be a single color or a list of colors).
        node_size : int or list, optional
            Size of the nodes (single value or list of sizes).
        edge_color : str or list, optional
            Color of the edges (can be a single color or a list of colors).
        width : float, optional
            Width of the edges.
        with_labels : bool, optional
            Whether to draw node labels or not.
        font_size : int, optional
            Size of the font for node labels.
        font_color : str, optional
            Color of the font for node labels.
        title : str, optional
            Title of the plot.
        seed : int, optional
            Seed for the random layout algorithm.
        figsize : tuple, optional
            Size of the figure.
        ax: axes object
            Axes object to draw the plot on. Defaults to None, which will create a new figure.
        pos: object, optional
            Graph layout (e.g., nx.spring_layout, nx.circular_layout), nx.kamada_kaway_layout(G). 
            Defaults to nx.spring_layout(G).

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
    ax = kwargs.get("ax", None)
    pos = kwargs.get("pos", None)

    if ax is None:
        fig, ax = plt.subplots(1, figsize=figsize)
        ax.axis("off")

    if seed is not None:
        np.random.seed(seed)  

    if pos is None:
        pos = nx.spring_layout(
            G, seed=seed
    )

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
        ax=ax
    )

    if edge_labels is not None:
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Set the plot title
    if title is not None:
        plt.title(title)
    
    return ax

    # Show the plot
    # plt.show()
