import heapq

from DiGraph import DiGraph
from Node import Node
import matplotlib.pyplot as plt


class visual_g:
    def __init__(self, graph: DiGraph):
        self.graph = graph
        self.left = []
        self.xq = []
        self.yq = []
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

        if len(self.left) == 0:
            return
        self.mk_q(xc, yc)
        # if self.left.__sizeof__() == self.graph.v_size():
        #     pass
        # else:
        #     pass

    def mk_q(self, xc: list, yc: list):
        for i in range(len(xc) - 1):
            cur = cor(xc[i], xc[i + 1])
            heapq.heappush(self.xq, cur)
            cur = cor(yc[i], yc[i + 1])
            heapq.heappush(self.yq, cur)
        heapq.heapify(self.xq)
        print(cor.get_dist(self.xq.pop()))
        print(cor.get_dist(self.xq.pop()))
        print(cor.get_dist(self.xq.pop()))
        print(cor.get_dist(self.xq.pop()))
        self.rnd_mk()

    def rnd_mk(self):
        x = 0
        y = 0
        while len(self.left):
            nod: Node = self.left.pop()
            cur: cor = self.xq.pop()[1]
            x = cur.coor1 + (cur.dist / 2)
            f = cor(cur.coor1, x)
            heapq.heappush(self.xq, (f.dist, f))
            f = cor(x, cur.coor2)
            heapq.heappush(self.xq, (f.dist, f))
            cur = self.yq.pop()[1]
            y = cur.coor1 + (cur.dist / 2)
            f = cor(cur.coor1, y)
            heapq.heappush(self.yq, (f.dist, f))
            f = cor(y, cur.coor2)
            heapq.heappush(self.yq, (f.dist, f))
            nod.set_pos(x, y)


class cor:
    def __init__(self, coor1: float, coor2: float):
        self.coor1 = coor1
        self.coor2 = coor2
        self.dist = abs(coor2 - coor1)

    def get_dist(self):
        return self.dist

    def __lt__(self, other):
        if self.dist == cor.get_dist(other):
            return 1
        return cor.get_dist(other) > self.dist

    def __eq__(self, other):
        if self.dist == cor.get_dist(other):
            return True

    def __cmp__(self, other):
        if self.dist == cor.get_dist(other):
            return 0
        if self.dist > cor.get_dist(other):
            return 1
        return -1