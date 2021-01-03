import json
from typing import List
import heapq
import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from Node import Node
from Tarjan import Tarjan


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
                    gr.add_node(dic["id"], dic["pos"])
                for dic in dict_graph["Edges"]:
                    gr.add_edge(id1=dic["src"], id2=dic["dest"], weight=dic["w"])
        except IOError as e:
            print(e)
            return False
        self.graph = gr
        return True

    def encoder(self, o):
        DiGraph.encoder(self.graph, o)

    def decoder(self):
        gp_dict = {"Edges": [],
                   "Nodes": [Node.encoder(node) for node in list(self.graph.get_all_v().values())]}
        for nd in self.graph.nodes.keys():
            for dest, wei in self.graph.all_out_edges_of_node(nd).items():
                gp_dict["Edges"].append({"src": nd, "w": wei, "dest": dest})
        return gp_dict

    def save_to_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "w") as f:
                json.dump(self.decoder(), fp=f, indent=4)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        if id1 == id2:
            return 0, path
        if id1 not in DiGraph.get_all_v(self.graph).keys() or id2 not in DiGraph.get_all_v(self.graph).keys():
            return float('inf'), []
        dest: Node = DiGraph.get_node(self.graph, id2)
        self.dijkstra(DiGraph.get_node(self.graph, id1), dest)
        dist = dest.get_tag()
        while dest.get_pred() is not None:
            path.insert(0, dest.get_key())
            dest = dest.get_pred()
        if dist != float('inf'):
            path.insert(0, dest.get_key())
        # if DiGraph.get_node(self.graph, id1) not in path:
        #     return float('inf'), []
        return dist, path

    def connected_component(self, id1: int) -> list:
        if self.graph is None:
            return []
        if id1 not in self.graph.nodes.keys():
            return []
        self.reset_t()
        t = Tarjan(self.graph, self.graph.get_node(id1))
        return t.get_nds_comp()

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        self.reset_t()
        t = Tarjan(self.graph)
        return t.get_components()

    def plot_graph(self) -> None:
        pass

    def dijkstra(self, src: Node, dest: Node):
        self.reset_d()
        src.set_tag(0)
        q = []
        for nd in self.graph.nodes.values():
            heapq.heappush(q, (Node.get_tag(nd), Node.get_key(nd), nd))
        while len(q) != 0:
            cur: Node = heapq.heappop(q)[2]
            for ni, ed in Node.get_ni(cur).items():
                ni_node: Node = DiGraph.get_node(self.graph, ni)
                if not ni_node.get_is_vis():
                    dis = Node.get_tag(cur) + ed
                    if Node.get_tag(ni_node) > dis:
                        Node.set_tag(ni_node, dis)
                        Node.set_pred(ni_node, cur)
                        heapq.heapify(q)
            if cur.get_key() == dest.get_key():
                return
            cur.set_is_vis(True)

    def reset_d(self):
        for nd in self.graph.nodes.values():
            Node.set_tag(nd, float('inf'))
            Node.set_pred(nd, None)
            Node.set_is_vis(nd, False)

    def reset_t(self):
        for nd in self.graph.nodes.values():
            Node.set_tag(nd, -1)
            Node.set_is_vis(nd, False)

    def __eq__(self, other):
        if type(other) is not GraphAlgo:
            return False
        if self.graph.__eq__(GraphAlgo.get_graph(other)):
            return True
        return False
