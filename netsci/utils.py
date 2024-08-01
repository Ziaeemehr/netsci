import numpy as np
import networkx as nx


def get_adjacency_list(G):
    """
    Generate an adjacency list representation of a given graph.

    Parameters:
    G (networkx.Graph, networkx.DiGraph): The input graph for which the adjacency list is to be generated.

    Returns:
    dict: A dictionary where each key is a node in the graph and the corresponding value is a list of neighboring nodes.
    """
    return {n: list(neighbors) for n, neighbors in G.adj.items()}


