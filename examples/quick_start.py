"""

First import the necessary libraries:

.. literalinclude:: ../examples/quick_start.py
    :start-after: example-st\u0061rt
    :lines: 1-4
    :dedent: 0

Next, create a simple graph with self-avoiding edges (SAE) between nodes.

.. literalinclude:: ../examples/quick_start.py
    :start-after: example-st\u0061rt
    :lines: 6-8


Now, find all self-avoiding paths from a given start node to a target node.

.. literalinclude:: ../examples/quick_start.py
    :start-after: example-st\u0061rt
    :lines: 11-16

Finally, visualize the graph.

.. literalinclude:: ../examples/quick_start.py
    :start-after: example-st\u0061rt
    :lines: 18
      
.. figure:: images/01.png
    :scale: 80 %
"""

# example-start
import networkx as nx
import matplotlib.pyplot as plt
from netsci.plot import plot_graph
from netsci.analysis import find_sap

G = nx.Graph()
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("E", "F")]
G.add_edges_from(edges)

# Find all self-avoiding paths from 'A' to 'F'
start_node = "A"
target_node = "F"
all_saps = list(find_sap(G, start_node, target_node))

for path in all_saps:
    print("->".join(path))

plot_graph(G, seed=2, figsize=(3, 3))
import os
os.makedirs("images", exist_ok=True)
plt.savefig("images/01.png", bbox_inches="tight")

# example-end
