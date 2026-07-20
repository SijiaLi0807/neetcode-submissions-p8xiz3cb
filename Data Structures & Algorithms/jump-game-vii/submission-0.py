class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # 前缀和优化 DP
        n = len(s)
        dp = [0] * n #能不能挑落到i？ false 视作 0，true 视作 1
        dp[0] = 1
        
        presum = [0] * n #  计算 dp 的前缀和数组 
        #在[max(0,i-maxJump),i-minJump]中存在true等价于和不为0\
        
        for i in range(minJump):
            # 由于我们从 i=minJump 开始动态规划，因此需要将 [0,minJump) 这部分的前缀和预处理出来
            presum[i] = 1

        for i in range(minJump,n):
            left, right = i-maxJump, i-minJump
            if s[i] == '0':
                total = presum[right] - (presum[left-1] if left>= 0 else 0)
                dp[i] = int(total !=0)
            presum[i] = presum[i-1] + dp[i]

        return bool(dp[n-1])     