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
        if node_id in self.nodes.keys():
            return False

        self.nodes[node_id] = Node(key=node_id, pos=pos)
        self.mode_count = self.mode_count + 1
        return True

    def remove_node(self, node_id: int) -> bool:
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
        self.mode_count = self.mode_count + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.nodes or node_id2 not in self.nodes or node_id1 == node_id2:
            return False
        if node_id2 in self.all_out_edges_of_node(node_id1).keys():
            self.edge_out[node_id1].pop(node_id2)
            self.edge_in[node_id2].pop(node_id1)
        self.mode_count = self.mode_count + 1
        self.num_of_ed = self.num_of_ed - 1
        return True

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
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
        self.mode_count = self.mode_count + 1
        self.num_of_ed = self.num_of_ed + 1
        return True

    def get_node(self, id_num):
        return self.nodes[id_num]

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 not in self.edge_in.keys():
            return {}
        return self.edge_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 not in self.edge_out.keys():
            return {}
        return self.edge_out.get(id1)

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.num_of_ed

    def get_mc(self) -> int:
        return self.mode_count

    @staticmethod
    def encoder(o):
        print(o.__dict__)
        return o.__dict__

    def __eq__(self, other):
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
        return f"Graph: |V|={self.v_size()} , |E|={self.num_of_ed}"

    def encoder(self):
        return {
            'Nodes': [nd.encoder() for nd in self.nodes.values()],
            'Edges': [{'src': sc, 'dest': ds, 'w': we} for sc in self.edge_out.keys() for ds, we in
                      self.edge_out[sc].items()]
        }


if __name__ == '__main__':
    ed = {int: {int: float}}
    ed[5] = {2: 3}
    ed[5].update({3: 6})
    print(ed[5][2])
