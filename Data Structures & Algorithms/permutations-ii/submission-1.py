class Solution:
    def backtracking(self, nums: List[int], used: List[int], path: List[int], res: List):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            if used[i]:
                continue
            used[i] = 1
            path.append(nums[i])
            self.backtracking(nums, used, path, res)
            used[i] = 0
            path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        self.backtracking(nums, [0]*len(nums), [], res)
        return res
        