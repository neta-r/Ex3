import heapq
from DiGraph import DiGraph
from Node import Node


class sp_algo:

    @staticmethod
    def dijkstra(graph: DiGraph, src: Node, dest: Node):
        sp_algo.reset_d(graph)
        src.set_tag(0)
        q = []
        for nd in graph.nodes.values():
            heapq.heappush(q, (Node.get_tag(nd), Node.get_key(nd), nd))
        while len(q) != 0:
            cur: Node = heapq.heappop(q)[2]
            for ni, ed in Node.get_ni(cur).items():
                ni_node: Node = DiGraph.get_node(graph, ni)
                if not ni_node.get_is_vis():
                    dis = Node.get_tag(cur) + ed
                    if Node.get_tag(ni_node) > dis:
                        Node.set_tag(ni_node, dis)
                        Node.set_pred(ni_node, cur)
                        heapq.heapify(q)
            if cur.get_key() == dest.get_key():
                return
            cur.set_is_vis(True)

    @staticmethod
    def reset_d(graph: DiGraph):
        for nd in graph.nodes.values():
            Node.set_tag(nd, float('inf'))
            Node.set_pred(nd, None)
            Node.set_is_vis(nd, False)

    @staticmethod
    def reset_t(graph: DiGraph):
        for nd in graph.nodes.values():
            Node.set_tag(nd, -1)
            Node.set_is_vis(nd, False)

    class Tarjan:

        def __init__(self, g: DiGraph, nd: Node = None):
            self.__time = 0
            self.__graph = g
            self.__st = []
            self.__comps = [[]]
            self.__nd = nd
            self.__nds_com = []

        def tar(self):
            sp_algo.reset_d(self.__graph)
            for nd in self.__graph.nodes.values():
                if not Node.get_is_vis(nd):
                    self.dfs(nd)

        def dfs(self, nd: Node):
            self.__time = self.__time + 1
            nd.set_tag(self.__time)
            nd.set_is_vis(True)
            self.__st.append(nd)
            is_component_root = True
            for key_n in self.__graph.all_out_edges_of_node(nd.get_key()).keys():
                nei = self.__graph.get_node(key_n)
                if not Node.get_is_vis(nei):
                    self.dfs(nei)
                if nd.get_tag() > Node.get_tag(nei):
                    nd.set_tag(Node.get_tag(nei))
                    is_component_root = False
            if is_component_root:
                com = []
                flag = False
                while True:
                    x = self.__st.pop()
                    if x == self.__nd:
                        flag = True
                    com.append(Node.get_key(x))
                    Node.set_tag(x, float('inf'))
                    if x == nd:
                        break
                self.__comps.append(com)
                if flag:
                    self.__nds_com = com
                    return

        def get_nds_comp(self):
            self.tar()
            return self.__nds_com

        def get_components(self):
            self.tar()
            self.__comps.pop(0)
            return self.__comps
