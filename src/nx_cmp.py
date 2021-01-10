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
        return gr


if __name__ == '__main__':
    v = [10, 100, 1000, 10000, 20000, 30000]
    e = [80, 800, 8000, 80000, 160000, 240000]
    a = GraphAlgo()
    for ve, ed in zip(v, e):
        print(f"Graph : |V|={ve} , |E| = {ed}")
        g = nx_cmp.read_json_file(f"../data/G_{ve}_{ed}_0.json")
        a.load_from_json(f"../data/G_{ve}_{ed}_0.json")
        print("CC of 1 ///////////////////////////////////////////")
        dt = time.time()
        f=a.connected_component(1)
        mt = time.time() - dt
        print(f"my time : {mt},Number of nodes in CC= {len(f)}")
        print("Shortest Path ////////////////////////////////////////\n")
        dt = time.time()
        f = a.shortest_path(1, 5)
        mt = time.time() - dt
        print(f"my time : {mt}, path size list for correct algo= {len(f[1])}")
        dt = time.time()
        f = nx.shortest_path(g, 1, 5, weight='weight')
        mt = time.time() - dt
        print(f"networkx time : {mt}, path size list for networkx algo= {len(f)}")
        print("Connected Components ////////////////////////////////////////////////////////\n")
        dt = time.time()
        f = a.connected_components()
        mt = time.time() - dt
        print(f"my time : {mt}, Number of SCC= {len(f)}")
        dt = time.time()
        f = nx.kosaraju_strongly_connected_components(g)
        mt = time.time() - dt
        print(f"networkx time : {mt},Number of SCC= {f}")

