import itertools
import numpy as np
import networkx as nx


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


def graph_info(G):
    """
    Generate various graph information.

    Parameters:
    G (networkx.Graph, networkx.DiGraph): The input graph for which the information is to be generated.

    Returns:
    dict: A dictionary containing the graph information.
    """
    is_directed = isinstance(G, nx.DiGraph)
    if is_directed:
        diameter = nx.diameter(G)
    else:
        diameter = np.nan

    return {
        "Directed": is_directed,
        "Number of nodes": len(G.nodes()),
        "Number of edges": len(G.edges()),
        "average_degree": sum(dict(G.degree).values()) / len(G.nodes),
        "diameter": diameter,
        "average clustering coefficient": nx.average_clustering(G),
        
    }
    
def average_degree(G):
    """
    Calculate the average degree of a graph.
    
    Parameters:
    G (networkx.Graph or networkx.DiGraph): The input graph, which can be directed or undirected.
    
    Returns:
    float: The average degree of the graph.
    """
    
    degrees = [d for n, d in G.degree()]
    average_degree = sum(degrees) / len(degrees)
    return average_degree
