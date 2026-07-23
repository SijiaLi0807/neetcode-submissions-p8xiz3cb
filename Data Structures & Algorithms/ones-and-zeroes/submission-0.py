class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for s in strs:
            x, y = 0, 0
            for c in s:
                if c =='0':
                    x+=1
                else:
                    y+=1
            for i in range(m,x-1,-1):
                for j in range(n,y-1,-1):
                    dp[i][j] = max(dp[i][j], dp[i-x][j-y]+1)

        return dp[m][n]
        
        