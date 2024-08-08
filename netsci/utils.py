import os
import gzip
import json
import numpy as np
import networkx as nx
from numpy import power
from os.path import join
from cycler import cycler
from scipy.special import zeta
from scipy.optimize import bisect


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


# def _load_graph(file_path, kind, url):

#     path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     path = os.path.join(path, 'netsci/datasets')

#     if not os.path.isfile(file_path):
#         os.system(f"wget -P {path} {url}")

#     if os.path.isfile(file_path):
#         os.system(f"gunzip -k {file_path}")

#     with gzip.open(file_path, 'rt') as f:
#         G = nx.read_adjlist(file_path, create_using=kind)

#     os.remove(file_path[:-3])
#     return G


def download_sample_dataset():
    url = "https://networksciencebook.com/translations/en/resources/networks.zip"
    path = get_sample_dataset_path()
    path_zip = join(path, "networks.zip")
    file_path = join(path, "collaboration.edgelist.txt")
    if not os.path.isfile(path_zip):
        os.system(f"wget -P {path} {url}")
    else:
        print(f"File {path_zip} already exists.")
    
    if not os.path.isfile(file_path):
        if os.path.isfile(path_zip):
            os.system(f"unzip {path_zip} -d {path}")
            print(f"Extracted {path_zip} to {path}")        



def _load_graph(file_path, url, directed, verbose=False):

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = join(path, "netsci/datasets")
    path_zip = join(path, "networks.zip")

    if not os.path.isfile(file_path):
        if not os.path.isfile(path_zip):
            os.system(f"wget -P {path} {url}")

    if not os.path.isfile(file_path):
        if os.path.isfile(path_zip):
            os.system(f"unzip {path_zip} -d {path}")

    # Step 1: Read the adjacency list from the file
    edges = []
    with open(file_path, "r") as file:
        for line in file:
            if line.startswith("#"):
                continue  # Skip comments
            A, B = map(int, line.split())
            edges.append((A, B))

    # Step 2: Create the graph
    G = nx.DiGraph()
    G.add_edges_from(edges)

    # Step 3: Determine if the graph is directed
    # is_directed = False
    # for A, B in edges:
    #     if not G.has_edge(B, A):
    #         is_directed = True
    #         break

    if not directed:
        G = G.to_undirected()
    return G


def load_sample_graph(name, verbose=False):
    """
    Load a graph and return it as a NetworkX graph.

    Parameters
    --------------
    name: str
        The name of the graph. Get names from `netsci.utils.show_sample_graphs()`.
    verbose: bool, optional
        If True, print information about the loaded graph. Default is True.

    Returns
    -----------
    value: networkx.Graph
        Loaded graph.
    """

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(path, "netsci/datasets/")

    with open(os.path.join(path, "sample_graphs.json"), "r") as f:
        data = json.load(f)
    if name in list(data.keys()):
        filename = data[name]["filename"]
        file_path = os.path.join(path, f"{filename}")
        directed = data[name]["directed"]
        G = _load_graph(
            file_path, url=data[name]["url"], directed=directed, verbose=verbose
        )
        if verbose:
            print(f"Successfully loaded {name}")
            print("================================")
            print(data[name]["description"])
        return G


def list_sample_graphs():
    """
    make a list of available real world graphs on datasets
    """

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(path, "netsci/datasets")
    # names = [f[:-7] for f in os.listdir(path) if f.endswith('.txt.gz')]
    # read json file sample_graphs.json

    with open(os.path.join(path, "sample_graphs.json"), "r") as f:
        data = json.load(f)

    return data


def generate_power_law_dist(N: int, a: float, xmin: float):
    """
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
    """

    # generates random variates of power law distribution
    vrs = powerlaw.Power_Law(xmin=xmin, parameters=[a]).generate_random(N)

    return vrs


def generate_power_law_dist_bounded(
    N: int, a: float, xmin: float, xmax: float, seed: int = -1
):
    """
    Generate a power law distribution of floats p(k) ~ x^(-a) for a>1
    which is bounded by xmin and xmax

    parameters :
        N: int
            number of samples in powerlaw distribution (pwd).
        a:
            exponent of the pwd.
        xmin:
            min value in pwd.
        xmax:
            max value in pwd.
    """

    from numpy.random import rand, randint
    from numpy import power

    data = np.zeros(N)
    x0p = power(xmin, (-a + 1.0))
    x1p = power(xmax, (-a + 1.0))
    alpha = 1.0 / (-a + 1.0)

    for i in range(N):
        r = rand()
        data[i] = power((x1p - x0p) * r + x0p, alpha)
    return data


def generate_power_law_discrete(
    N: int, a: float, xmin: float, xmax: float, seed: int = -1
):
    """
    Generate a power law distribution of p(k) ~ x^(-a) for a>1,
    with discrete values.

    Parameters:
    -----------
    N: int
        Number of samples in the distribution.
    a: float
        Exponent of the power law distribution.
    xmin: float
        Minimum value in the power law distribution.
    xmax: float
        Maximum value in the power law distribution.
    seed :int, optional
        Seed for reproducibility. Defaults to -1.

    Returns:
    -------
    np.array
        Power law distribution with discrete values.
    """

    if seed != -1:
        np.random.seed(seed)

    if seed != None:
        np.random.seed(seed)

    X = np.zeros(N, dtype=int)
    x1p = power(xmax, (-a + 1.0))
    x0p = power(xmin, (-a + 1.0))
    alpha = 1.0 / (-a + 1.0)

    for i in range(N):
        r = np.random.rand()
        X[i] = int(np.round(power(((x1p - x0p) * r + x0p), alpha)))

    # sum of degrees should be positive
    from random import randint

    if (np.sum(X) % 2) != 0:
        i = randint(0, N - 1)
        X[i] = X[i] + 1

    return X


def tune_min_degree(N: int, a: float, xmin: int, xmax: int, max_iteration: int = 100):
    """
    Find the minimum degree value of a power law graph that results in a connected graph
    """

    for i in range(max_iteration):
        seq = generate_power_law_discrete(N, a, xmin, xmax, seed=i)
        if np.sum(seq) % 2 != 0:
            raise ValueError("The sum of degrees should be even")
        G = nx.configuration_model(seq)
        G.remove_edges_from(G.selfloop_edges())
        G = nx.Graph(G)
        seq1 = np.asarray([deg for (node, deg) in G.degree_iter()])
        avg_degree = np.mean(seq1)

        if nx.is_connected(G):
            break
    if i == (max_iteration - 1):
        raise ValueError("Unable to find a connected graph with the given parameters")
    return avg_degree, G


def make_powerlaw_graph(
    N: int,
    a: float,
    avg_degree: int,
    xmin: int = 1,
    xmax: int = 10000,
    seed: int = -1,
    xtol=0.01,
    degree_interval=5.0,
    plot=False,
    **kwargs,
):
    """
    make a powerlaw graph with the given parameters

    Parameters
    ----------
    N:
        number of nodes
    a: float
        exponent of the power law distribution
    avg_degree:
        expected average degree
    xmin: int, optional
        minimum value in the power law distribution. Default is 1.
    xmax: int, optional
        maximum value in the power law distribution. Default is 10000.
    seed: int, optional
        Seed for reproducibility. Default is -1.
    xtol: float, optional
        tolerance for bisection method. Default is 0.01.
    degree_interval: float, optional
        interval for bisection method. Default is 5.0.
    plot: bool, optional
        If True, plot the power law distribution. Default is False.
    kwargs: obtional
        additional keyword arguments for plot_pdf function.

    """

    color = kwargs.get("color", "k")
    linestyle = kwargs.get("linestyle", "-")
    lw = kwargs.get("lw", 2)

    xmin_tuned, G = bisect(
        lambda x: tune_min_degree(N, a, x, xmax) - avg_degree,
        xmin,
        xmin + degree_interval,
        xtol=xtol,
    )
    sample_seq = np.asarray([deg for (node, deg) in G.degree_iter()])
    avg_degree = np.mean(sample_seq)

    fit = powerlaw.Fit(sample_seq, discrete=True)
    if plot:
        ax = fit.plot_pdf(linewidth=2, label=str("pdf, %.2f" % a))
        fit.power_law.plot_pdf(c=color, linestyle=linestyle, lw=lw, ax=ax)

    return {
        "G": G,
        "avg_degree": avg_degree,
        "xmin_tuned": xmin_tuned,
        "fit": fit,
        "ax": ax,
    }


def generate_power_law_discrete_its(
    alpha: float, k_min: int, k_max: int, size: int = 1
):
    """
    Generates the power law discrete distributions using the inverse transform sampling method.

    References
    -----------

    Devroye, L. (1986). "Non-Uniform Random Variate Generation." Springer-Verlag, New York.

    Parameters
    ----------
    alpha :
        Power law exponent.
    k_min :
        Minimum degree.
    k_max :
        Maximum degree.
    size :
        Number of samples to generate. Defaults to 1.

    Returns
    -------
    np.array:
        Array of generated power law discrete distributions.


    Examples
    ---------

    >>> gamma = 2.5  # Power-law exponent
    >>> k_min = 1    # Minimum value of k
    >>> k_max = 1000 # Maximum value of k
    >>> size = 10000 # Number of samples
    >>> samples = power_law_discrete(gamma, k_min, k_max, size)
    """

    # Calculate the normalization constant
    norm = zeta(alpha, k_min) - zeta(alpha, k_max + 1)

    # Generate uniform random numbers
    u = np.random.random(size=size)

    # Initialize the result array
    result = np.zeros(size, dtype=int)

    # Inverse transform sampling
    for i in range(size):
        cdf = 0
        for k in range(k_min, k_max + 1):
            cdf += (k**-alpha) / norm
            if u[i] <= cdf:
                result[i] = k
                break

    return result


def get_sample_dataset_path():
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(path, "netsci/datasets/")
    return path