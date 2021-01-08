import heapq
from DiGraph import DiGraph
from Node import Node


class sp_algo:

    @staticmethod
    def dijkstra(graph: DiGraph, src: Node, dest: Node):
        sp_algo.reset_d(graph)
        src.set_tag(0)
        vis = set()
        unvis = [(0, src)]
        while len(unvis) and len(vis) != graph.v_size():
            cur: Node = heapq.heappop(unvis)[1]
            if cur.get_key() not in vis:
                vis.add(cur.get_key())
                if cur.get_key() == dest.get_key():
                    return
                for ni, ed in graph.all_out_edges_of_node(cur.get_key()).items():
                    ni_node: Node = DiGraph.get_node(graph, ni)
                    dis = cur.get_tag() + ed
                    if ni_node.get_tag() > dis:
                        ni_node.set_tag(dis)
                        ni_node.set_pred(cur)
                        unvis.append((ni_node.get_tag(), ni_node))
                heapq.heapify(unvis)

    @staticmethod
    def reset_d(graph: DiGraph):
        for nd in graph.nodes.values():
            # Node.set_tag(nd, float('inf'))
            nd.set_tag(float('inf'))
            nd.set_pred(None)

    @staticmethod
    def reset_t(graph: DiGraph):
        for nd in graph.nodes.values():
            nd.set_tag(-1)
            nd.set_pred(None)

    class Tarjan:

        def __init__(self, g: DiGraph, nd: Node = None):
            self.__time = 0
            self.__graph = g
            self._vis = set()
            self.__st = []
            self.__comps = [[]]
            self.__nd = nd
            self.__nds_com = []

        def tar(self, cmp: Node = None):
            sp_algo.reset_d(self.__graph)
            if cmp is not None:
                self.dfs(cmp)
                return
            for nd in self.__graph.nodes.values():
                if nd.get_key() not in self._vis:
                    self.dfs(nd)

        def dfs(self, nd: Node):
            #unvis= [nd.get_key()]
            self.__time = self.__time + 1
            nd.set_tag(self.__time)
            self._vis.add(nd.get_key())
            self.__st.append(nd)
            is_component_root = True

            for key_n in self.__graph.all_out_edges_of_node(nd.get_key()).keys():
                nei: Node = self.__graph.get_node(key_n)
                if key_n not in self._vis:
                    self.dfs(nei)
                if nd.get_tag() > nei.get_tag():
                    nd.set_tag(nei.get_tag())
                    is_component_root = False
            if is_component_root:
                com = []
                flag = False
                while True:
                    x = self.__st.pop()
                    if x == self.__nd:
                        flag = True
                    com.insert(0, x.get_key())
                    Node.set_tag(x, float('inf'))
                    if x == nd:
                        break
                self.__comps.insert(1, com)
                if flag:
                    self.__nds_com = com
                    return

        def get_nds_comp(self):
            self.tar(self.__nd)
            return sorted(self.__nds_com)

        def get_components(self):
            self.tar()
            self.__comps.pop(0)
            return self.__comps
