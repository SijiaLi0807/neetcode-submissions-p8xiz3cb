class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cur = next = res = i =0
        n = len(nums)
        while i < n:
            next = max(next,i+nums[i])
            if i == cur:
                if cur !=n-1:
                    res +=1
                    cur=next
                    if cur >= n-1:
                        return res
            i+=1