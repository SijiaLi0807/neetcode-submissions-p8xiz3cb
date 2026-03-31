class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path =[], []
        n = len(nums)
        def backtesting(startindex):
            nonlocal nums, path
            res.append(path[:])#为什么不是path？因为path时可变的m，所以 res 里之前保存的“答案”也会跟着一起变，最后全都变成同一个最终状态（通常都是 []）。
            for i in range(startindex,n):
                path.append(nums[i])
                backtesting(i+1)
                path.pop()
        backtesting(0)
        return res