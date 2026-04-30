class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        while j < n:
            target = nums[j]
            nums[i] = target
            i+=1
            j+=1
            while j < n and nums[j] == target:
                j+=1
        return i
            
