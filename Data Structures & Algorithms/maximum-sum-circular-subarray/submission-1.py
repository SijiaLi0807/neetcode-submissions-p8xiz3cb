class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_f = 0     # 计算最大子数组和的 DP 数组（空间优化成一个变量）
        max_s = float("-inf")  # 最大子数组和，不能为空
        min_f = 0     # 计算最小子数组和的 DP 数组（空间优化成一个变量）
        min_s = 0     # 最小子数组和，可以为空（元素和为 0）

        for x in nums:
            # 53. 最大子数组和（空间优化写法）
            max_f = max(max_f, 0) + x
            max_s = max(max_s, max_f)
            min_f = min(min_f, 0) + x
            min_s = min(min_s, min_f)

        if max_s < 0:
            return max_s
        return max(max_s, sum(nums) - min_s)

# https://leetcode.cn/problems/maximum-sum-circular-subarray/solutions/2351107/mei-you-si-lu-yi-zhang-tu-miao-dong-pyth-ilqh