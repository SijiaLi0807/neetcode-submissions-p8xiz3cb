class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = i = 0 
        n = len(nums)
        if n <= 1:
            return True
        while i <= cover and i < n:  
            cover = max(cover,i+nums[i])
            i = i+1
        if cover < n-1:
            return False
        else:
            return True