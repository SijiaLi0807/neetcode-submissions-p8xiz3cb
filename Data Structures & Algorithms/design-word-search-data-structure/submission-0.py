class WordDictionary:

    def __init__(self):
        self.isEnd = False
        self.next = [None] * 26

    def addWord(self, word: str) -> None:
        node = self
        for w in word:
            idx = ord(w) - ord('a')

            if not node.next[idx]:
                node.next[idx] = WordDictionary()

            node = node.next[idx]

        node.isEnd = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            for i in range(index, len(word)):
                w = word[i]

                if w == '.':
                    for child in node.next:
                        if child and dfs(i + 1, child): #用dfs：因为每个存在的next都要试试
                            return True
                    return False

                else:
                    idx = ord(w) - ord('a')

                    if not node.next[idx]:
                        return False

                    node = node.next[idx]

            return node.isEnd

        return dfs(0, self)