class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        for l in range(n-2):
            if l!= 0 and nums[l] == nums[l-1]:
                continue 
            r = n-1
            for m in range(l+1,n-1): 
                if m!= l+1 and nums[m] == nums[m-1]:
                    continue 
                target = - nums[l] - nums[m]
                while m < r and nums[r] > target:
                    r -=1
                if m == r:
                    continue #为什么换成while m < r+1就错
                if nums[r] == target:
                    ans.append([nums[l],nums[m],nums[r]])  
                if nums[r] < target:
                    continue
        return ans
