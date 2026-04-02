class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = dict()
        n = len(nums)
        if n == 1:
            return nums[0]
        target = n/2
        for num in nums:
            if num in seen:
                seen[num] +=1
                if seen[num] > target:
                    return num
            else:
                seen[num] = 1