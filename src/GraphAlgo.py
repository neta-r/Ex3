import json
from typing import List

import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def encoder(self, o):
        DiGraph.encoder(self.graph, o)

    def save_to_json(self, file_name: str) -> bool:
        a = self.graph.nodes
        try:
            with open(file_name, "w") as fp:
                json.dump(self.graph.nodes, default=self.encoder, fp=fp, indent=4)
                return True
        except IOError as e:
            print(e)
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
