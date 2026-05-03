class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans, total = n+1, 0
        l, r = 0, 0
        while r < n:
            total+=nums[r]
            while total >= target:
                ans = min(ans, r-l+1)
                total-=nums[l]
                l+=1
            r+=1
                
        return ans if ans!=(n+1) else 0
