class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [0] * (n + 1)
        ans[1] = nums[0]

        for i in range(2,n+1):
            ans[i] = max(ans[i-1], ans[i-2] + nums[i-1])  
            
        return ans[n]
        