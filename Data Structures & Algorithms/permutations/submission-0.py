class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtracking(used,path,res):
            nonlocal n
            if len(path) == n:
                res.append(path[:]) 
                return
            for i in range(n):
                if used[i] == 1:
                    continue
                path.append(nums[i])
                used[i] = 1
                backtracking(used,path,res)
                path.pop()
                used[i] = 0
        backtracking([0]*n, [], res)
        return res
