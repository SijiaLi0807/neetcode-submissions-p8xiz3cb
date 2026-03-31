class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans = [0]
        for i,num in enumerate(nums):
            if num == 1 + nums[i-1]:
                ans[-1] += 1
            elif i != 0 and num == nums[i-1]:
                continue
            else:
                ans.append(1)
    
        return max(ans)