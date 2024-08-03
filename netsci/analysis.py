import itertools
import numpy as np
import networkx as nx


def find_sap(G, start, target, path=None):
    
    """
    Finds all self-avoiding paths (SAPs) in a given graph from a start node to a target node.
    A self-avoiding path is a path that does not revisit any node.

    Parameters
    ----------
    graph : NetworkX graph
        The input graph where SAPs will be found.
    start : str or int
        The node where the search for SAPs starts.
    target : str or int
        The node where the search for SAPs ends.
    path : list, optional
        Internal parameter used to keep track of the current path during the search.

    Yields
    ------
    list
        A self-avoiding path from the start node to the target node.

    Examples
    --------
    >>> import networkx as nx
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
        
    if len(G.nodes()) == 0:
        return []

    path.append(start)

    if start == target:
        yield path[:]
    else:
        for neighbor in G.neighbors(start):
            if neighbor not in path:
                yield from find_sap(G, neighbor, target, path)

    path.pop()


def is_hamiltonian_path(G, path):
    '''
    Check if a given path is a Hamiltonian path in a graph.
    
    Parameters:
    -----------
    G : networkx.Graph, networkx.DiGraph)
        The input graph.
    path : list of str or int
        list of nodes in the path.
    
    Returns:
    -----------
    bool : 
        True if the path is a Hamiltonian path, otherwise False
    
    '''
    return all(G.has_edge(path[i], path[i + 1]) for i in range(len(path) - 1))


def find_hamiltonian_path(G):
    '''
    find the Hamiltonian path in given graph.
    
    Parameters
    -----------
    G: nx.Graph or nx.DiGraph
        input graph.
    
    Returns
    value : list of nodes in Hamiltonian path if exists, otherwise None.
    
    '''
    nodes = list(G.nodes())
    for perm in itertools.permutations(nodes):
        if is_hamiltonian_path(G, perm):
            return perm
    return None


def check_connectivity(G):
    '''
    Check if the graph is connected.
    
    Parameters
    --------------
    G : networkx.Graph, networkx.DiGraph
        The input graph.
    
    Returns
    ------------
    
    connectivity: (str)
        for directed graphs, it returns 
        - "weakly connected"
        - "strongly connected"
        - "disconnected".
        for undirected graphs, 
        - "connected" 
        - "disconnected".
    '''
    
    is_directed = isinstance(G, nx.DiGraph)
    
    if is_directed:
        if nx.is_weakly_connected(G):
            return "weakly connected"
        elif nx.is_strongly_connected(G):
            return "strongly connected"
        else:
            return "disconnected"
    else:
        if nx.is_connected(G):
            return "connected"
        else:
            return "disconnected"

def graph_info(G, quick=True):
    """
    Generate various graph information.

    Parameters
    -------------
    G : (networkx.Graph, networkx.DiGraph)
        The input graph for which the information is to be generated.

    
    """
    is_directed = isinstance(G, nx.DiGraph)
    
    # number_of_triangles = #TODO
    
    connectivity = check_connectivity(G)
    
    if not quick:
        if connectivity == "strongly connected" or connectivity == "connected":
            diameter = nx.diameter(G)
        else:
            diameter = -1
        
    print("Graph information")
    print(f"{'Directed':40s}: {str(is_directed):>20s}")
    print(f"{'Number of nodes':40s}: {len(G.nodes()):20d}")
    print(f"{'Number of edges':40s}: {len(G.edges()):20d}")
    print(f"{'Average degree':40s}: {sum(dict(G.degree).values()) / len(G.nodes):20.4f}")
    print(f"{'Connectivity':40s}: {connectivity:>20s}")
    if not quick:
        print(f"{'Diameter':40s}: {diameter:20d}")
        print(f"{'Average clustering coefficient':40s}: {nx.average_clustering(G):20.6f}")
        
    # return {
    #     "Directed": is_directed,
    #     "Number of nodes": len(G.nodes()),
    #     "Number of edges": len(G.edges()),
    #     "average_degree": sum(dict(G.degree).values()) / len(G.nodes),
    #     "diameter": diameter,
    #     "average clustering coefficient": nx.average_clustering(G),
        
    # }
    
def longest_shortest_path(G):
    """
    Calculate the longest shortest path (diameter) in a given graph.

    Parameters
    -------------
    G (networkx.Graph or networkx.DiGraph): 
        The input graph, which can be directed or undirected.
        The graph should be connected, otherwise the diameter will not be defined.

    Returns:
    value : int, float
        The longest shortest path (diameter) in the graph.
        If the graph is empty, returns 0.
        If the graph is not connected, returns float('inf').
    """
    path_lengths = dict(nx.all_pairs_shortest_path_length(G))
    diameter = max(max(lengths.values()) for lengths in path_lengths.values())
    
    return diameter

    
def average_degree(G):
    """
    Calculate the average degree of a graph.
    
    Parameters
    -------------
    G (networkx.Graph or networkx.DiGraph): 
        The input graph, which can be directed or undirected.
    
    Returns:
    vlaue: float
        The average degree of the graph.
    """
    
    degrees = [d for n, d in G.degree()]
    average_degree = sum(degrees) / len(degrees)
    return average_degree
