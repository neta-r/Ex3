class Node:
    random_key = 0

    def __init__(self, key: int = random_key, pos: tuple = None):
        self.random_key = self.random_key+1
        self.key = key
        self.nei = {}
        self.pos = pos

    def get_key(self) -> int:
        return self.key

    def get_ni(self) -> dict:
        return self.nei

    def add_ni(self, other_key: int, weight: float):  # נצטרך בחיבור של שני הקודקודים לשלוח פעמיים לפונקציה הזאת
        if type(other_key) != int:
            return
        if other_key not in self.nei: # להסביר לטל למה עשיתי ככה
            self.nei[other_key] = weight

    def remove_ni(self, other_key: int): # נצטרך בחיבור של שני הקודקודים לשלוח פעמיים לפונקציה הזאת
        if type(other_key) != int:
            return
        if other_key in self.nei:
            del self.nei[other_key]

    def get_ni(self):
        return self.nei.keys()


