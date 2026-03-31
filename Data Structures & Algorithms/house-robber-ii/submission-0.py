class Solution:
    def rob1(self, Nums: List[int]) -> int:
        '''
        如果偷 nums[0]，那么 nums[1] 和 nums[n−1] 不能偷，问题变成从 nums[2] 到 nums[n−2] 的非环形版本，调用 198 题的代码解决；
        如果不偷 nums[0]，那么问题变成从 nums[1] 到 nums[n−1] 的非环形版本，同样调用 198 题的代码解决。
        '''
        n = len(Nums)
        if n == 0:
            return 0
        ans = [0] * (n + 1)
        ans[1] = Nums[0]

        for i in range(2,n+1):
            ans[i] = max(ans[i-1], ans[i-2] + Nums[i-1])  
            
        return ans[n]

    def rob(self, nums: List[int]) -> int:
        return max(nums[0] + self.rob1(nums[2:-1]), self.rob1(nums[1:]))