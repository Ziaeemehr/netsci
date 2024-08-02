import os
import gzip
import json
import numpy as np
import networkx as nx

try:
    import powerlaw
except:
    pass


def get_adjacency_list(G):
    """
    Generate an adjacency list representation of a given graph.

    Parameters
    -------------
    G (networkx.Graph, networkx.DiGraph): 
        The input graph for which the adjacency list is to be generated.

    Returns
    ---------
    value: dict 
        A dictionary where each key is a node in the graph and the corresponding value is a list of neighboring nodes.
    """
    return {n: list(neighbors) for n, neighbors in G.adj.items()}


def _load_graph(file_path, kind, url):
    
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(path, 'netsci/datasets')
    
    if not os.path.isfile(file_path):
        os.system(f"wget -P {path} {url}")
        
    if os.path.isfile(file_path):
        os.system(f"gunzip -k {file_path}")
    
    with gzip.open(file_path, 'rt') as f:
        G = nx.read_adjlist(file_path, create_using=kind)
    
    os.remove(file_path[:-3]) 
    return G
    

def load_sample_graph(name, verbose=True):
    """
    Load a graph and return it as a NetworkX graph.

    Parameters
    --------------
    name (str): 
        The name of the graph. Get names from `netsci.utils.show_sample_graphs()`.

    Returns
    -----------
    value: networkx.Graph
        The loaded graph.
    """
    
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(path, 'netsci/datasets')
    
    with open(os.path.join(path,'sample_graphs.json'), 'r') as f:
        data = json.load(f)
    if name in list(data.keys()):
        file_path = os.path.join(path, f'{name}.txt.gz')
        directed = data[name]['directed']
        kind = nx.DiGraph if directed else nx.Graph            
        G = _load_graph(file_path, kind, url=data[name]['url'])
        if verbose:
            print(f'Successfully loaded {name}')
            print('================================')
            print(data[name]['description'])
        return G
        
    
def show_sample_graphs():
    '''
    make a list of available real world graphs on datasets
    '''
    
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(path, 'netsci/datasets')
    # names = [f[:-7] for f in os.listdir(path) if f.endswith('.txt.gz')]
    # read json file sample_graphs.json
    
    with open(os.path.join(path,'sample_graphs.json'), 'r') as f:
        data = json.load(f)
    
    return data
    
    
def generate_power_law_dist_bounded(N:int, a:float, xmin:float, xmax:float):
    '''
    Generate a power law distribution of floats p(k) ~ x^(-a) for a>1
    which is bounded by xmin and xmax
    
    parameters :
        N: int
            number of samples in powerlaw distribution (pwd).
        e: 
            exponent of the pwd.
        xmin: 
            min value in pwd.
        xmax: 
            max value in pwd.
    '''

    from numpy.random import rand, randint
    from numpy import power

    data = np.zeros(N)
    x0p = power(xmin, (a+1.0))
    x1p = power(xmax, (a+1.0))
    alpha = 1.0/(a+1.0)

    for i in range(N):
        r = rand()
        data[i] = (power((x1p - x0p)*r + x0p, alpha))
    return data


def generate_power_law_dist(N:int, a:float, xmin:float):
    '''
    generate power law random numbers p(k) ~ x^(-a) for a>1
    
    Parameters
    -----------
    N:
        is the number of random numbers
    a:
        is the exponent
    xmin:
        is the minimum value of distribution
    
    Returns
    -----------
    value: np.array
        powerlaw distribution
    '''
    
    # generates random variates of power law distribution
    vrs = powerlaw.Power_Law(xmin=xmin, parameters=[a]).generate_random(N)

    return vrs