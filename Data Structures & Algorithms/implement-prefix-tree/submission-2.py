class PrefixTree:
    def __init__(self):
        self.isEnd = False
        self.next = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for s in word:
            s = ord(s) - ord("a")
            if not node.next[s]:
                node.next[s] = PrefixTree()
            node = node.next[s] 
        node.isEnd = True 

    def search(self, word: str) -> bool:
        node = self
        for s in word:
            s = ord(s) - ord("a")
            if not node.next[s]:
                return False
            node = node.next[s] 
        return True if node.isEnd else False 
        

    def startsWith(self, prefix: str) -> bool:
        node = self
        for s in prefix:
            s = ord(s) - ord("a")
            if not node.next[s]:
                return False
            node = node.next[s] 
        return True 
        