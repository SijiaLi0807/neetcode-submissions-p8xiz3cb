class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        times_n = Counter(nums)
        if any(value>1 for key, value in times_n.items()):
            return True
        else:
            return False