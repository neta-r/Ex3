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
        """
        returns: The graph this class operates on.
        """
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        """
        This function loads the graph from a json format to an object of a GraphAlgo.
        returns: True if the action succeeded, False otherwise.
        """
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
        """
        This function sets the logic to building a json object out of GraphAlgo.
        note: Will be used in the save function.
        """
        gp_dict = {"Edges": [],
                   "Nodes": [Node.encoder(node) for node in list(self.graph.get_all_v().values())]}
        for nd in self.graph.nodes.keys():
            for dest, wei in self.graph.all_out_edges_of_node(nd).items():
                gp_dict["Edges"].append({"src": nd, "w": wei, "dest": dest})
        return gp_dict

    def save_to_json(self, file_name: str) -> bool:
        """
        This function saves the current graph into a json format, Uses the logic sets by the encoder function.
        returns: True if the action succeeded, False otherwise.
        """
        try:
            with open(file_name, "w") as f:
                json.dump(self.encoder(), fp=f, indent=4)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        This is the casing function of the Dijkstra function in the sp_algo class.
        The function operates iff the two vertices are unequals by keys and both of them exists in the graph.
        The function builds the path from the pred field saved in each node after the Dijkstra operates.
        returns: The distance between the two vertices and the path to get there.
        note: If there is no valid path the function will return float('inf') and an empty path.
        """
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
        """
        This is the casing function of the Tarjan function in the sp_algo class.
        The function operates iff the vertex exists in the graph and the graph exists.
        returns: A list of vertices that shares the same SCC with the given vertex.
        note: If the given vertex doesn't exist in the graph or the graph doesn't exists the function will return an empty list.
        """
        if self.graph is None:
            return []
        if id1 not in self.graph.nodes.keys():
            return []
        t = sp_algo.Tarjan(self.graph, self.graph.get_node(id1))
        return t.get_nds_comp()

    def connected_components(self) -> List[list]:
        """
        This is the casing function of the Tarjan function in the sp_algo class.
        The function operates iff the the graph exists.
        returns: A list of lists- each inner list contains all the vertices that are sharing the same SCC.
        note: If the graph doesn't exists the function will return an empty list.
        """
        if self.graph is None:
            return []
        t = sp_algo.Tarjan(self.graph)
        return t.get_components()

    def plot_graph(self) -> None:
        """
        This is the casing function of the paint function in the visual_g class.
        """
        a = visual_g(self.graph)
        a.run()

    def __eq__(self, other):
        """
        returns: True if the two AlgoGraphs are equals by all the GraphAlgo's fields.
        note: Will be use in the tests.
        """
        if type(other) is not GraphAlgo:
            return False
        if self.graph.__eq__(GraphAlgo.get_graph(other)):
            return True
        return False
