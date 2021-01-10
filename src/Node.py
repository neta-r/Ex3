class Node(object):
    random_key = 0

    def __init__(self, key: int = random_key, pos: tuple = None):
        Node.random_key = self.random_key + 1
        self.__key = key
        self.__pos = pos
        self.__tag = -1
        self.__pred = None
        self.num_of_ed_in = 0
        self.num_of_ed_out = 0

    def get_key(self) -> int:
        """
        returns: The key of the vertex.
        """
        return self.__key

    def get_tag(self) -> int:
        """
        returns: The tag of the vertex.
        note: Will be used later in the Dijkstra and Tarjan algorithms.
        """
        return self.__tag

    def set_tag(self, tag):
        """
        parm: A new tag to the vertex.
        note: Will be used later in the Dijkstra and Tarjan algorithms.
        """
        self.__tag = tag

    def get_pred(self):
        """
        returns: The predecessor of the vertex.
        note: Will be used later in the Dijkstra algorithm.
        """
        return self.__pred

    def set_pred(self, pred):
        """
        parm: A new predecessor of the vertex.
        note: Will be used later in the dijkstra algorithm.
        """
        self.__pred = pred

    def get_pos(self) -> [tuple]:
        """"
        returns: The position (x and y) of the vertex.
        note: Will be used later to draw the graph.
        """
        return self.__pos

    def set_pos(self, x, y):
        """
        parm: A new position of the vertex.
        note: Will be used later to draw the graph.
        """
        self.__pos = (x, y, 0)

    def __str__(self):
        """
        returns: A String representing the vertex.
        """
        return f"str: id:{self.__key}, pos:{self.__pos}"

    def __repr__(self):
        """
        returns: A String representing the vertex.
        """
        return f"{self.__key}: |edges out| {self.num_of_ed_out} |edges in| {self.num_of_ed_in}"  # , pos:{self.__pos}"

    def encoder(self):
        """
        returns: The representation of the vertex in a json format.
        """
        if self.__pos is None:
            return {
                'id': self.get_key()}
        return {
            'id': self.get_key(),
            'pos': self.__pos
        }

    def __lt__(self, other):
        """
        returns: Which vertex is bigger.
        note: Will be used later in a priority queue.
        """
        other: Node = other
        if self.__tag == other.__tag:
            return True
        else:
            return self.__tag < other.__tag

    def __eq__(self, other):
        """
        returns: True if the two vertices are equals by all the node's fields.
        note: Will be use in the tests.
        """
        if type(other) is not Node:
            return False
        if Node.get_key(other) != self.__key:
            return False
        if self.__pos != Node.get_pos(other):
            return False
        return True
