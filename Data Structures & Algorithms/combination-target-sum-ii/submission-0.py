class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        used = [0]* n
        candidates.sort()
        #candidates = candidates.sort()
        def backtesting(startindex, total, path):#, used):
            nonlocal target, n, res, candidates
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(startindex,n):
                if i > startindex and candidates[i] == candidates[i-1]: #不是i >0，这样会把例如[1,1]的结果去掉
                    continue
                path.append(candidates[i])
                total += candidates[i]
                backtesting(i+1,total, path)
                path.pop()
                total -= candidates[i]
        backtesting(0,0,[])
        return res