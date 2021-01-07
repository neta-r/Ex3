import json
from typing import List
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from Node import Node
from sp_algo import sp_algo
from visual_g import visual_g
import threading


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=None):
        self.graph: DiGraph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        gr = DiGraph()
        try:
            with open(file_name, "r") as f:
                dict_graph = json.load(f)
                for dic in dict_graph["Nodes"]:
                    try:
                        st = dic["pos"]
                        x, y, z = str.split(st, ",")
                        x = float(x)
                        y = float(y)
                        z = float(z)
                        gr.add_node(dic["id"], (x, y, z))
                    except Exception:
                        gr.add_node(dic["id"])
                for dic in dict_graph["Edges"]:
                    gr.add_edge(id1=dic["src"], id2=dic["dest"], weight=dic["w"])
        except IOError as e:
            print(e)
            return False
        self.graph = gr
        return True

    def encoder(self):
        gp_dict = {"Edges": [],
                   "Nodes": [Node.encoder(node) for node in list(self.graph.get_all_v().values())]}
        for nd in self.graph.nodes.keys():
            for dest, wei in self.graph.all_out_edges_of_node(nd).items():
                gp_dict["Edges"].append({"src": nd, "w": wei, "dest": dest})
        return gp_dict

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as f:
                json.dump(self.encoder(), fp=f, indent=4)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        if id1 == id2:
            return 0, path
        if id1 not in DiGraph.get_all_v(self.graph).keys() or id2 not in DiGraph.get_all_v(self.graph).keys():
            return float('inf'), path
        dest: Node = DiGraph.get_node(self.graph, id2)
        sp_algo.dijkstra(self.graph, DiGraph.get_node(self.graph, id1), dest)
        dist = dest.get_tag()
        while dest.get_pred() is not None:
            path.insert(0, dest.get_key())
            dest = dest.get_pred()
        if dist != float('inf'):
            path.insert(0, dest.get_key())
        return dist, path

    def connected_component(self, id1: int) -> list:
        if self.graph is None:
            return []
        if id1 not in self.graph.nodes.keys():
            return []
        t = sp_algo.Tarjan(self.graph, self.graph.get_node(id1))
        return t.get_nds_comp()

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        t = sp_algo.Tarjan(self.graph)
        return t.get_components()

    def plot_graph(self) -> None:
        a = visual_g(self.graph)
        #t1 = threading.Thread(target=a.run)##TODO:make the thread die
        #t1.start()
        a.run()
        print("what?")

    def __eq__(self, other):
        if type(other) is not GraphAlgo:
            return False
        if self.graph.__eq__(GraphAlgo.get_graph(other)):
            return True
        return False
