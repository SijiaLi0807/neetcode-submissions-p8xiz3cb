class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[i][j] means the i-th day is in the j-th state.

    	dp[i][0]: hold the position
        dp[i][1]: no position (we can buy) 
        dp[i][2]: sell the stock (followed by cooldown)
        dp[i][3]: cooldown
        '''
        n = len(prices)
        dp = [[0]* 4 for _ in range(n)]
        dp[0][0] = -prices[0]

        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][3]-prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0]+prices[i]
            dp[i][3] = dp[i-1][2]
        return max(dp[n-1][0],dp[n-1][1],dp[n-1][2],dp[n-1][3])