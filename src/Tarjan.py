from DiGraph import DiGraph
from Node import Node


class Tarjan:

    def __init__(self, g: DiGraph, nd: Node = None):
        self.__time = 0
        self.__graph = g
        self.__st = []
        self.__comps = [[]]
        self.__nd = nd
        self.__nds_com = []

    def tar(self):
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

    def get_nds_comp(self):
        self.tar()
        return self.__nds_com

    def get_components(self):
        self.tar()
        self.__comps.pop(0)
        return self.__comps
