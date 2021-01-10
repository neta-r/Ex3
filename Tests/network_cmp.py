import json
import networkx as nx
from networkx.readwrite import json_graph
from unittest import TestCase

from cl.GraphAlgo import GraphAlgo


class network_cmp(TestCase):
    @staticmethod
    def read_json_file(filename: str):
        with open(filename) as f:
            js_graph = json.load(f)
        return json_graph.node_link_graph(js_graph, directed=True)

    def test_runtime(self):
        k = GraphAlgo()
        k.load_from_json("../data/G_30000_240000_0.json")
        g:nx.DiGraph=k.get_graph()

        print("who?")
        print("what?")
