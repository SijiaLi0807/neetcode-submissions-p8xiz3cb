class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = res = float('-inf')
        for i,num in enumerate(nums):
            if res < 0 or i ==0:
                res = num
            else:
                res += num
            ans = max(ans,res)
        return ans

        