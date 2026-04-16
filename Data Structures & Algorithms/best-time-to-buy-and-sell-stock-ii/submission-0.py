class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[i][0]: no position
        dp[i][1]: have position
        1. how to transit to 0
        dp[i][0] = max{dp[i-1][0], price[i] + dp[i-1][1]} 
        2. transit to 1
        dp[i][1] = max{dp[i-1][1] + dp[i-1][0] - price[i]}
对于初始状态，根据状态定义我们可以知道第 0 天交易结束的时候 dp[0][0]=0，dp[0][1]=−prices[0]。

因此，我们只要从前往后依次计算状态即可。由于全部交易结束后，持有股票的收益一定低于不持有股票的收益，因此这时候 dp[n−1][0] 的收益必然是大于 dp[n−1][1] 的，最后的答案即为 dp[n−1][0]。
        '''
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = - prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][0]-prices[i], dp[i-1][1])
        return dp[n-1][0]