class Node(object):
    random_key = 0

    def __init__(self, key: int = random_key, pos: tuple = None):
        self.random_key = self.random_key + 1
        self.__key = key
        self.__nei = {}
        self.__c_to_me = {}
        self.__pos = pos
        self.__tag = -1
        self.__is_vis = False
        self.__pred = None

    def get_key(self) -> int:
        return self.__key

    def get_tag(self) -> int:
        return self.__tag

    def set_tag(self, tag):
        self.__tag = tag

    def get_pred(self):
        return self.__pred

    def set_pred(self, pred):
        self.__pred = pred

    def get_is_vis(self) -> bool:
        return self.__is_vis

    def set_is_vis(self, is_vis):
        self.__is_vis = is_vis

    def get_pos(self) -> [tuple]:
        return self.__pos

    def get_ni(self):
        return self.__nei

    def get_c_tome(self):
        return self.__c_to_me

    def add_ni(self, other_node, weight: float):
        if Node.get_key(other_node) not in self.__nei.keys():  # להסביר לטל למה עשיתי ככה
            self.__nei[Node.get_key(other_node)] = weight
            Node.add_to_me(other_node, self, weight)

    def add_to_me(self, other_node, weight: float):
        self.__c_to_me[Node.get_key(other_node)] = weight

    def remove_ni(self, other_node):
        if Node.get_key(other_node) in self.__nei.keys():
            del self.__nei[Node.get_key(other_node)]
            Node.del_from_me(other_node, self)

    def del_from_me(self, other_node):
        del self.__c_to_me[Node.get_key(other_node)]

    # def __dict__(self):
    #     return {"id": self.__key, "pos": self.__pos}
    def __str__(self):
        return f"str: id:{self.__key}, pos:{self.__pos}"

    def __repr__(self):
        return f"repr: id:{self.__key}, pos:{self.__pos}"

    def encoder(self):
        return {
            'id': self.get_key(),
            'pos': self.__pos
        }

    def __eq__(self, other):
        if type(other) is not Node:
            return False
        if Node.get_key(other) != self.__key:
            return False
        if self.__pos != Node.get_pos(other):
            return False
        for nei, wei in self.__nei.items():
            if nei not in Node.get_ni(other):
                return False
            if Node.get_ni(other)[nei] != wei:
                return False
        for nei, wei in self.__c_to_me.items():
            if nei not in Node.get_c_tome(other):
                return False
            if Node.get_c_tome(other)[nei] != wei:
                return False
        return True
