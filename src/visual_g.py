from queue import PriorityQueue
from DiGraph import DiGraph
from Node import Node
import matplotlib.pyplot as plt


class visual_g:
    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.left = []
        self.xq = PriorityQueue()
        self.yq = PriorityQueue()
        self.org()

    def org(self):
        xc = []
        yc = []
        for nd in self.graph.get_all_v().values():
            nd: Node = nd
            if nd.get_pos() is not None:
                xc.append(nd.get_pos()[0])
                yc.append(nd.get_pos()[1])
            else:
                self.left.append(nd)
        if len(self.left) == 0:
            return
        xc.sort()
        yc.sort()
        if len(self.left) < self.graph.v_size():
            xc.insert(0, xc[0] - 0.5)
            xc.insert(len(xc), xc[len(xc) - 1] + 0.5)
            yc.insert(0, yc[0] - 0.5)
            yc.insert(len(yc), yc[len(yc) - 1] + 0.5)
        else:
            xc.insert(0, 0)
            xc.append(7)
            yc.insert(0, 0)
            yc.append(7)
        self.mk_q(xc, yc)

    def mk_q(self, xc: list, yc: list):
        for i in range(len(xc) - 1):
            cur = cor(xc[i], xc[i + 1])
            self.xq.put((-cur.dist, cur))
            cur = cor(yc[i], yc[i + 1])
            self.yq.put((-cur.dist, cur))
        self.rnd_mk()

    def rnd_mk(self):
        while len(self.left):
            nod: Node = self.left.pop()
            cur: cor = self.xq.get()[1]
            x = cur.coor1 + (cur.dist / 2)
            f = cor(cur.coor1, x)
            self.xq.put((-f.dist, f))
            f = cor(x, cur.coor2)
            self.yq.put((-f.dist, f))
            cur = self.yq.get()[1]
            y = cur.coor1 + (cur.dist / 2)
            f = cor(cur.coor1, y)
            self.xq.put((-f.dist, f))
            f = cor(y, cur.coor2)
            self.xq.put((-f.dist, f))
            nod.set_pos(x, y)

    def paint(self):
        x = []
        y = []
        plt.figure(figsize=(10, 5), facecolor="silver")
        ax = plt.axes()
        # plt.figure(figsize=(10, 10))
        for node in self.graph.nodes.values():
            x.append(node.get_pos()[0])
            y.append(node.get_pos()[1])
            # for ed in self.graph.all_out_edges_of_node(node.get_key()).keys():
            #     desti: Node = self.graph.get_node(ed)
            #     plt.arrow(node.get_pos()[0], node.get_pos()[1], desti.get_pos()[0], desti.get_pos()[1])
        ax.scatter(x, y, color="black", s=50)
        xl = ax.get_xlim()[1] - ax.get_xlim()[0]
        yl = ax.get_ylim()[1] - ax.get_ylim()[0]
        for nd in self.graph.nodes.values():
            for ed in self.graph.all_out_edges_of_node(Node.get_key(nd)).keys():
                desti: Node = self.graph.get_node(ed)
                destx = desti.get_pos()[0] - nd.get_pos()[0]
                desty = desti.get_pos()[1] - nd.get_pos()[1]
                ax.arrow(nd.get_pos()[0], nd.get_pos()[1], destx, desty, head_width=xl * 0.007,
                         length_includes_head=True,
                         head_length=yl * 0.02, width=xl * 0.0001 * yl, color='grey')
        plt.title("Your graph!")
        # plt.plot(x,y)
        plt.show()

    def run(self):
        self.paint()

class cor:
    def __init__(self, coor1: float, coor2: float):
        self.coor1 = coor1
        self.coor2 = coor2
        self.dist = abs(coor2 - coor1)

    def get_dist(self):
        return self.dist

    def __eq__(self, other):
        if self.dist == cor.get_dist(other):
            return True

    def __cmp__(self, other):
        if self.dist == cor.get_dist(other):
            return 0
        if self.dist > cor.get_dist(other):
            return 1
        return -1

