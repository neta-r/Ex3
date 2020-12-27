from GraphInterface import GraphInterface
from Node import Node

class DiGraph(GraphInterface):

    def __init__(self):
        self.nodes = {}
        self.num_of_ed = 0
        self.mode_count = 0

    def v_size(self) -> int:
        return len(self.nodes)

    def e_size(self) -> int:
        return self.num_of_ed

    def get_mc(self) -> int:
        return self.mode_count

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.nodes or id2 not in self.nodes or id1==id2:
            return False

        self.mode_count = self.mode_count+1
        # חסר פה בדיקה אם הצלע קיימת וחיבור שלה
        # להשלים!!!!!!!!!!!!!!!!!!!!!!


    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = Node(key=node_id, pos=pos)
        self.mode_count = self.mode_count+1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False # שלחתי הודעה בפורום לבדוק מה נסגר עם זה
        # פה אמורה לבוא שורה שמעיפים את כל השכנים של הקודקוד
        del self.nodes[node_id]
        self.mode_count = self.mode_count+1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.nodes or node_id2 not in self.nodes or node_id1 == node_id2:
            return False
        # חסר פה בדיקה אם הצלע קיימת וניתוק שלה
        # להשלים!!!!!!!!!!!!!!!!!!!!!!
        self.mode_count = self.mode_count+1

    def get_all_v(self) -> dict:
        return self.nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        pass

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass
