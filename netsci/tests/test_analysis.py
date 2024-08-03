import random
import unittest
import networkx as nx
from netsci.analysis import *


class TestFindSAP(unittest.TestCase):
    def test_empty_graph(self):
        G = nx.Graph()
        start_node = "A"
        target_node = "B"
        all_saps = list(find_sap(G, start_node, target_node))
        self.assertEqual(all_saps, [])

    def test_directly_connected_nodes(self):
        G = nx.Graph()
        edges = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "F"), ("E", "F")]
        G.add_edges_from(edges)
        start_node = "A"
        target_node = "B"
        all_saps = list(find_sap(G, start_node, target_node))
        self.assertEqual(len(all_saps), 2)
        self.assertEqual(all_saps[0], ["A", "B"])

    def test_graphs_with_cycles(self):
        G = nx.Graph()
        edges = [
            ("A", "B"),
            ("A", "C"),
            ("B", "D"),
            ("B", "E"),
            ("C", "F"),
            ("E", "F"),
            ("F", "G"),
            ("G", "A"),
        ]
        G.add_edges_from(edges)
        start_node = "A"
        target_node = "G"
        all_saps = list(find_sap(G, start_node, target_node))
        expected_paths = [["A", "B", "E", "F", "G"], ["A", "C", "F", "G"], ["A", "G"]]
        self.assertEqual(len(all_saps), len(expected_paths))
        for path in all_saps:
            self.assertIn(path, expected_paths)

    def test_disconnected_components(self):
        G = nx.Graph()
        edges = [("A", "B"), ("A", "C"), ("D", "E")]
        G.add_edges_from(edges)
        start_node = "A"
        target_node = "E"
        all_saps = list(find_sap(G, start_node, target_node))
        self.assertEqual(all_saps, [])

    def test_find_sap_with_different_node_types(self):
        G = nx.Graph()
        edges = [("A", 1), ("A", "B"), (1, 2), ("B", "C"), (2, 3), ("C", "D"), (1, "D")]
        G.add_edges_from(edges)
        start_node = "A"
        target_node = "D"
        all_saps = list(find_sap(G, start_node, target_node))
        expected_paths = [["A", 1, "D"], ["A", "B", "C", "D"]]

        self.assertEqual(len(all_saps), len(expected_paths))
        for path in all_saps:
            self.assertIn(path, expected_paths)


    def test_large_graph(self):
        G = nx.Graph()
        num_nodes = 50
        num_edges = 50
        edges = [
            (str(i), str(j)) for i in range(num_nodes) for j in range(i + 1, num_nodes)
        ]
        G.add_edges_from(random.sample(edges, num_edges))
        start_node = "1"
        target_node = "45"
        all_saps = list(find_sap(G, start_node, target_node))
        self.assertTrue(len(all_saps) > 0)
        for path in all_saps:
            self.assertEqual(len(path), len(set(path)))  # Check for no revisiting nodes


if __name__ == "__main__":
    unittest.main()
