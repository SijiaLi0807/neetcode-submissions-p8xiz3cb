class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2 # ensure the value is int
        dp = [0] * (target+1)
        
        for n in nums:
            for j in range(target,n-1,-1):
                dp[j] = max(dp[j-n]+n,dp[j])
        return dp[-1] == target