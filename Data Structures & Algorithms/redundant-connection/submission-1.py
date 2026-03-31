class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = list(range(len(edges)+1))

        def find(x: int) ->int:
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for a, b in edges:
            pa, pb = find(a), find(b)
            if pa == pb:
                return [a,b]
            p[pa] = pb
