class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #nums = sorted(nums)
        n = len(nums)
        if n ==0:
            return 0
        ans = float("-inf")
        #有一种可能是subarray只有1个值
        for l in range(n):
            for r in range(l,n):
                ans = max(ans,math.prod(nums[l:r+1]))
        return ans 


        