class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s = sum(nums)
        if abs(target) > s:
            return 0
        if (target +s)%2:
            return 0
        l = (target + s)//2
        n = len(nums)
        dp = [0]*(l+1) #可省略判断j - nums[i]
        dp[0] = 1
        for num in nums: #遍历物品放在外循环，遍历背包在内循环            
            for j in range(l,num-1,-1): #倒序保证物品只使用一次。
                #什么时候更新（累加）dp值？
                #背包容量j小于等于目标l且大于等于物品值
                dp[j] += dp[j-num]
        return dp[l]
