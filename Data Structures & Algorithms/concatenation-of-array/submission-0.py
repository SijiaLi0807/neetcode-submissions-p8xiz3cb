class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        #直接版
        #nums.extend(nums)
        ans = nums[:]
        for n in nums:
            ans.append(n)
        return ans