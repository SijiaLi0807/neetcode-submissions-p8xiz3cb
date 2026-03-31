class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, n = [], len(nums)
        def backtracking(path, res, startindex):
            nonlocal n, nums
            res.append(path[:])
            for i in range(startindex,n):
                if i > startindex and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtracking(path, res, i+1)
                path.pop()
        backtracking([],res,0)
        return res
                