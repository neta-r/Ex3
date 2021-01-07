import json
import networkx as nx
from networkx.readwrite import json_graph
from unittest import TestCase
import time
from GraphAlgo import GraphAlgo


class nx_cmp:
    @staticmethod
    def read_json_file(filename: str):
        gr = nx.DiGraph()
        try:
            with open(filename, "r") as f:
                dict_graph = json.load(f)
                for dic in dict_graph["Nodes"]:
                    gr.add_node(dic["id"])
                for dic in dict_graph["Edges"]:
                    gr.add_edge(dic["src"], dic["dest"], weight=dic["w"])
        except IOError as e:
            print(e)
        # self.graph = gr
        return gr


if __name__ == '__main__':
    a = GraphAlgo()
    a.load_from_json("../data/G_30000_240000_0.json")
    dt = time.time()
    f = a.shortest_path(5,1)
    mt = time.time() - dt
    print(mt)
    print(f[1])
    g = nx_cmp.read_json_file("../data/G_30000_240000_0.json")
    dt = time.time()
    n = nx.shortest_path(g, 5,1)
    nt = time.time() - dt
    print(n)
    print(nt)
    # k = nx.strongly_connected_components(g)
    i = 0
    # print(nx.number_strongly_connected_components(g))
    # for l in k:
    #     i += 1
    #     print(i)
    # print()
    print("what?")
