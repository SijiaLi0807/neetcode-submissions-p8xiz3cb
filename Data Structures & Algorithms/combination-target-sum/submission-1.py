class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        n = len(nums)
        def backtesting(startindex, total):
            nonlocal res, path, target, n
            if total > target: 
                return
            if total == target:
                res.append(path[:])
                return
            for i in range(startindex,n):
                path.append(nums[i])
                total += nums[i]
                backtesting(i,total)
                path.pop()
                total -= nums[i]
        backtesting(0, 0)
        return res