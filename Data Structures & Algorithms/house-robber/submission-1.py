class Solution:
    def rob(self, nums: List[int]) -> int:
        cur, pre = 0, 0
        for num in nums:
            cur, pre = max(pre + num, cur), cur #旧的pre相当于n-2,旧的cur相当于n-1
        return cur
        