class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # initialize
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]

        # 计算第一列的路径数
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        
        # 计算第一行的路径数
        for j in range(n):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1
        
        # recursion
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]