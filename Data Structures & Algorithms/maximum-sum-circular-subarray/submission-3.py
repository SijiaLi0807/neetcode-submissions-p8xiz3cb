class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        #空间优化版本，基础见53
        maxans = float('-inf')
        maxS = 0
        minans = 0
        minS = 0

        for num in nums:
            maxS = max(maxS,0)+num
            maxans = max(maxans, maxS)
            minS = min(minS,0)+num
            minans = min(minans, minS)
        
        #if maxans < 0:
        #这两个条件是等价的
        if sum(nums) == minans:
            return maxans
        
        return max(maxans, sum(nums) - minans)

        

# https://leetcode.cn/problems/maximum-sum-circular-subarray/solutions/2351107/mei-you-si-lu-yi-zhang-tu-miao-dong-pyth-ilqh
