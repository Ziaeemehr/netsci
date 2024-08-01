import os
import gzip
import numpy as np
import networkx as nx


def get_adjacency_list(G):
    """
    Generate an adjacency list representation of a given graph.

    Parameters
    -------------
    G (networkx.Graph, networkx.DiGraph): 
        The input graph for which the adjacency list is to be generated.

    Returns:
    value: dict 
        A dictionary where each key is a node in the graph and the corresponding value is a list of neighboring nodes.
    """
    return {n: list(neighbors) for n, neighbors in G.adj.items()}


def load_internet_graph():
    '''
    Load the P2P-Gnutella04 graph from the Stanford Network Analysis Project (SNAP).
    
    References 
    - https://snap.stanford.edu/data/#communities
    '''
    
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(path, 'netsci/datasets')
    
    file_path = os.path.join(path, 'p2p-Gnutella04.txt.gz')
    os.system(f"gunzip -k {file_path}")
    with gzip.open(file_path, 'rt') as f:
        G = nx.read_adjlist(file_path)
    
    os.remove(file_path[:-3]) 
    return G
    

def load_sample_graph(name):
    """
    Load a graph and return it as a NetworkX graph.

    Parameters
    --------------
    name (str): 
        The name of the graph including:
        - 'internet' 

    Returns
    -----------
    value: networkx.Graph
        The loaded graph.
    """
    
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(path, 'netsci/datasets')
    # print(path)
    
    if name == 'internet':
        return load_internet_graph()        
        