class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 空间优化ver
        # 基础见62，五、空间优化
        # https://leetcode.cn/problems/unique-paths/solutions/3062432/liang-chong-fang-fa-dong-tai-gui-hua-zu-o5k32

        m, n = len(grid), len(grid[0])
        #initialization
        f = [grid[0][0]]* n
        for i in range(1,n):
            f[i] = f[i-1]+ grid[0][i]

        #recursion
        for i in range(1,m):
            f[0] += grid[i][0]
            for j in range(1,n):
                f[j] = min(f[j], f[j-1])+grid[i][j]
        
        return f[n-1]
