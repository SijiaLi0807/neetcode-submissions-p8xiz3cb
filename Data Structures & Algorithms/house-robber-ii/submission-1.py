class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(nums) -> int:
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            dp = [0] * n
            dp[0], dp[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
            return dp[n-1]
        if len(nums) < 2:
            return nums[0]
        list1, list2, list3 = nums[:-1], nums[1:-1],  nums[1:]
        return max(rob1(list1),rob1(list2),rob1(list3))