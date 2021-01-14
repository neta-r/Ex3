from GraphInterface import GraphInterface
from Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.num_of_ed = 0
        self.mode_count = 0
        self.edge_in = {int: {int: float}}
        self.edge_out = {int: {int: float}}

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        This function is adding a vertex to the graph if it's key doesn't exist already.
        returns: True if the action succeeded, False otherwise.
        """
        if node_id in self.nodes.keys():
            return False

        self.nodes[node_id] = Node(key=node_id, pos=pos)
        self.mode_count = self.mode_count + 1
        return True

    def remove_node(self, node_id: int) -> bool:
        """
        This function is removing a vertex from the graph if it's key exist.
        The function will also disconnect all of the vertex' edges in and out.
        returns: True if the action succeeded, False otherwise.
        """
        bef_mc=self.mode_count
        if node_id not in self.nodes.keys():
            return False
        if node_id in self.edge_out.keys():
            id = list(self.all_out_edges_of_node(node_id).keys())
            for ed in id:
                self.remove_edge(node_id, ed)
            self.edge_out.pop(node_id)
        if node_id in self.edge_in.keys():
            id = list(self.all_in_edges_of_node(node_id).keys())
            for ed in id:
                self.remove_edge(ed, node_id)
            self.edge_in.pop(node_id)
        del self.nodes[node_id]
        self.mode_count = bef_mc + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        This function is disconnecting between two vertices according to their keys.
        The function will perform iff the two keys given exists in the graph and there is an edge between them.
        returns: True if the action succeeded, False otherwise.
        """
        if node_id1 not in self.nodes or node_id2 not in self.nodes or node_id1 == node_id2:
            return False
        if node_id2 in self.all_out_edges_of_node(node_id1).keys():
            self.get_node(node_id1).num_of_ed_out -= 1
            self.get_node(node_id2).num_of_ed_in -= 1
            self.edge_out[node_id1].pop(node_id2)
            self.edge_in[node_id2].pop(node_id1)
        self.mode_count = self.mode_count + 1
        self.num_of_ed = self.num_of_ed - 1
        return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        This function is connecting between two vertices according to their keys.
        The function will perform iff the two keys given exists in the graph and there is no edge between them.
        note: If there is an edge it will *not* be change.
        returns: True if the action succeeded, False otherwise.
        """
        if id1 not in self.nodes or id2 not in self.nodes or id1 == id2:
            return False
        if id2 in self.all_out_edges_of_node(id1).keys():
            return False
        if id1 not in self.edge_out:
            self.edge_out[id1] = {id2: weight}
        else:
            self.edge_out[id1].update({id2: weight})
        if id2 not in self.edge_in:
            self.edge_in[id2] = {id1: weight}
        else:
            self.edge_in[id2].update({id1: weight})
        self.get_node(id1).num_of_ed_out += 1
        self.get_node(id2).num_of_ed_in += 1
        self.mode_count = self.mode_count + 1
        self.num_of_ed = self.num_of_ed + 1
        return True

    def get_node(self, id_num):
        """
        returns: A specific vertex in the graph by it's key.
        """
        if id_num in self.nodes:
            return self.nodes[id_num]

    def get_all_v(self) -> dict:
        """
        returns: A dictionary of all the vertices in the graph.
        """
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        returns: A dictionary of all the edges coming out of a vertex by it's key.
        The dictionary's keys are the vertex' neighbors' keys,
        and the dictionary's values are the weight of the edges between the two vertices.
        """
        if id1 not in self.edge_in.keys():
            return {}
        return self.edge_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        returns: A dictionary of all the edges coming in the vertex by it's key.
        The dictionary's keys are the vertex' neighbors' keys,
        and the dictionary's values are the weight of the edges between the two vertices.
        """
        if id1 not in self.edge_out.keys():
            return {}
        return self.edge_out.get(id1)

    def v_size(self) -> int:
        """
        returns: The number of edges in the graph.
        """
        return len(self.nodes)

    def e_size(self) -> int:
        """
        returns: The number of vertices in the graph.
        """
        return self.num_of_ed

    def get_mc(self) -> int:
        """
        returns: The number of changes that were made in the graph.
        Changes can be:
        - Adding and removing vertices.
        - Connecting and disconnecting vertices.
        """
        return self.mode_count

    def __eq__(self, other):
        """
        returns: True if the two graphs are equals by all the DiGraph's fields.
        note: Will be use in the tests.
        """
        if type(other) is not DiGraph:
            return False
        if self.e_size() != DiGraph.e_size(other):
            return False
        if self.v_size() != DiGraph.v_size(other):
            return False
        if self.get_mc() != DiGraph.get_mc(other):
            return False
        for nd in self.nodes.values():
            if nd.get_key() not in other.get_all_v().keys():
                return False
            other_v = other.get_node(nd.get_key())
            if not nd == other_v:
                return False
            if nd.get_key() not in self.edge_out.keys():
                continue
            for nei1, ed1 in self.edge_out[nd.get_key()].items():
                if nei1 in other.edge_out[nd.get_key()].keys():
                    if ed1 != other.edge_out[nd.get_key()].get(nei1):
                        return False
        return True

    def __repr__(self):
        """
        returns: The representation of the graph in a json format.
        """
        return f"Graph: |V|={self.v_size()} , |E|={self.num_of_ed}"

