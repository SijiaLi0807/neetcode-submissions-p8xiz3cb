class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, v in enumerate(nums):
            if i > k:
                seen.remove(nums[i-k-1])
            if v in seen:
                return True
            seen.add(v)
        return False
                

