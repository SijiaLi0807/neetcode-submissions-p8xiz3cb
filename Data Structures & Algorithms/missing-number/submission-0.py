class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i,n in enumerate(nums):
            if i !=n:
                return i
        return len(nums)
