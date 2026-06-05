class Solution:
    def backtracking(self, n: int, k: int, startidx: int, res: list, path: list):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(startidx, n-(k-len(path))+2):
            path.append(i)
            self.backtracking(n,k,i+1, res, path)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(n, k, 1, res, [])
        return res
