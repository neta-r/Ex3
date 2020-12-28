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
        if type(other_node) != Node:
            return
        if Node.get_key(other_node) not in self.__nei:  # להסביר לטל למה עשיתי ככה
            self.__nei[other_node] = weight
            Node.add_to_me(other_node, self.get_key(), weight)

    def add_to_me(self, other_key: int, weight: float):
        self.__c_to_me[other_key] = weight

    def remove_ni(self, other_node):
        if type(other_node) != Node:
            return
        if Node.get_key(other_node) in self.__nei:
            del self.__nei[other_node]
            Node.del_from_me(other_node, self.get_key())

    def del_from_me(self, other_key: int):
        del self.__c_to_me[other_key]
