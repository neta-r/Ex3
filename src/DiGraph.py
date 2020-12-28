from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {int: Node}
        self.num_of_ed = 0
        self.mode_count = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.num_of_ed

    def get_mc(self) -> int:
        return self.mode_count

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes or id2 not in self.nodes or id1 == id2:
            return False
        if id2 in Node.get_ni(self.nodes[id1]).keys():
            return False
        Node.add_ni(self.nodes[id1], id2, weight)
        self.mode_count = self.mode_count + 1
        self.num_of_ed = self.num_of_ed+1
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(key=node_id, pos=pos)
        self.mode_count = self.mode_count + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        while Node.get_c_tome(self.nodes[node_id]).__len__() != 0:
            src = list(Node.get_c_tome(self.nodes[node_id]).keys())[0]
            self.remove_edge(src, node_id)
        while Node.get_ni(self.nodes[node_id]).__len__() != 0:
            dst = list(Node.get_ni(self.nodes[node_id]).keys())[0]
            self.remove_edge(node_id,dst)
        del self.nodes[node_id]
        self.mode_count = self.mode_count + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.nodes or node_id2 not in self.nodes or node_id1 == node_id2:
            return False
        if node_id2 in Node.get_ni(self.nodes[node_id1]).keys():
            return False
        Node.remove_ni(self.nodes[node_id1], node_id1)
        Node.remove_ni(self.nodes[node_id1], node_id1)
        self.mode_count = self.mode_count + 1
        self.num_of_ed= self.num_of_ed-1
        return True

    def get_node(self, id_num):
        return self.nodes[id_num]

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return Node.get_ni(self.nodes[id])

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

# להחליף לגרף מכוון
