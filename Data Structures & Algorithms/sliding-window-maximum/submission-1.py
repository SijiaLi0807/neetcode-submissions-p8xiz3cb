class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1
        ans = [0] * n
        for i in range(n):
            ans[i] = max(nums[i:i+k])
        return ans
        