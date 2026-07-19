class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dpynamic programming
        '''
        n = len(nums)
        dp = [0]* (n+1)
        
        for i in range(n):
            dp[i+1] = max(dp[i],0) + nums[i]
        return max(dp)
        '''
        #空间优化:计算dp[i]只会用到dp[i-1]
        ans = float('-inf')
        dp = 0
        for num in nums:
            dp = max(dp, 0) + num
            ans = max(ans, dp)
        return ans


#https://leetcode.cn/problems/maximum-subarray/solutions/2533977/qian-zhui-he-zuo-fa-ben-zhi-shi-mai-mai-abu71