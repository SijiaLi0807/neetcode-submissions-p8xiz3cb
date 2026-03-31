class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        stack_size = 0
        for n in nums:
            if n != val:
                nums[stack_size] = n
                stack_size +=1
        return stack_size