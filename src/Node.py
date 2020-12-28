class Node:
    random_key = 0

    def __init__(self, key: int = random_key, pos: tuple = None):
        self.random_key = self.random_key + 1
        self.__key = key
        self.__nei = {}
        self.__c_to_me = {}
        self.__pos = pos

    def get_key(self) -> int:
        return self.__key

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
