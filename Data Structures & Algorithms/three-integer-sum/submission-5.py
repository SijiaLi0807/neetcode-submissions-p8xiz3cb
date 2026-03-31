class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        n = len(nums)
        #f,t = 0,n - 1
        for f in range(n):
            if f != 0 and nums[f] == nums[f-1]:
                continue 
            t = n - 1
            for s in range(f+1,n):
                if s != f+1 and nums[s] == nums[s-1]:
                    continue
                target = - 1 * (nums[f]+nums[s])

                while s < t:
                    if nums[t] < target: 
                        break
                    if nums[t] == target: 
                        ans.append([nums[f],nums[s],nums[t]])
                        break
                    t -=1
        return ans

