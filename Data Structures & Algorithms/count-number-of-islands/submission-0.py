class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 邻接矩阵
        d = [[0,1],[0,-1],[1,0],[-1,0]]
        m, n = len(grid), len(grid[0])

        visited = [[False] * n for _ in range(m)]
        def dfs(grid, visited, x, y):
            for i, j in d:
                nextx = x + i
                nexty = y + j
                if nextx >= m or nextx < 0 or nexty >= n or nexty < 0:
                    continue
                # 未访问的陆地，标记并调用深度优先搜索
                if not visited[nextx][nexty] and grid[nextx][nexty] == '1':
                    visited[nextx][nexty] = True
                    dfs(grid, visited, nextx, nexty)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]: # 判断：如果当前节点是陆地，res+1并标记访问该节点，使用深度搜索标记相邻陆地。
                    res += 1
                    visited[i][j] = True
                    dfs(grid, visited, i, j)
        return res

        