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
        """
        This is the function that Organize the frame size.
        First it is dividing all of the vertices into two groups-
        Vertices with positions and vertices without positions.
        The default frame size in 7 X 7 (in case that all the vertices in the graph has no position).
        Otherwise the frame size is the maximum and minimum x and y  plus and minus 0.5 accordingly.
        Vertices with no position are sent to rnd_mk.
        """
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
        """
        This is the function that is creating cor objects out of each two adjacent x's and y's.
        """
        for i in range(len(xc) - 1):
            cur = cor(xc[i], xc[i + 1])
            self.xq.put((-cur.dist, cur))
            cur = cor(yc[i], yc[i + 1])
            self.yq.put((-cur.dist, cur))
        self.rnd_mk()

    def rnd_mk(self):
        """
        This is the function that random the position to the vertices that have none.
        It is doing it by taking the largest space between each adjacent x's and setting the vertex' x to be the middle
        of the section. Then it is doing the same with the largest space between each adjacent y's.
        Then it is dividing the used section into half and placing them back in the priority queue.
        """
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
        """
        This function draws the graph using the matplotlib library.
        The vertices are draw by using the scatter function and the edge by using the arrow function.
        """
        x = []
        y = []
        plt.figure(figsize=(10, 5), facecolor="silver")
        ax = plt.axes()
        for node in self.graph.nodes.values():
            x.append(node.get_pos()[0])
            y.append(node.get_pos()[1])
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
        plt.show()

    def run(self):
        self.paint()

class cor:
    def __init__(self, coor1: float, coor2: float):
        self.coor1 = coor1
        self.coor2 = coor2
        self.dist = abs(coor2 - coor1)

    def get_dist(self):
        """
        returns: The distance between a pair of coor.
        """
        return self.dist

    def __eq__(self, other):
        """
        returns: True if the two cor are equals by all the cor's fields.
        note: Will be use in the priority queue.
        """
        if self.dist == cor.get_dist(other):
            return True

    def __cmp__(self, other):
        """
        returns: 0 if the two cors are have the same distance,
        1 if the self cor has a bigger distance, and -1 if the self cor has a smaller distance.
        """
        if self.dist == cor.get_dist(other):
            return 0
        if self.dist > cor.get_dist(other):
            return 1
        return -1

