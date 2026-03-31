class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [] 
        for i in range(len(nums)):
            pro = 1
            for j in range(len(nums)):
                if j != i:
                    pro *= nums[j]
                else:
                    continue
            ans.append(pro)
        return ans

        