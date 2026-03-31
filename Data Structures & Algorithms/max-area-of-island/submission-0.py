class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        d = [[1,0],[-1,0],[0,1],[0,-1]]
        n, m = len(grid), len(grid[0])
        visited = [[False]* m for _ in range(n)] 
        maxans = 0
        ans = 0
        def dfs(grid,visited,x,y):
            nonlocal ans
            for i, j in d:
                nextx = x+i
                nexty = y+j
                if nextx <0 or nextx >=n or nexty <0 or nexty >=m:
                    continue
                if grid[nextx][nexty] and not visited[nextx][nexty]:
                    ans +=1
                    visited[nextx][nexty] = True
                    dfs(grid,visited,nextx,nexty)
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    visited[i][j] = True
                    ans = 1
                    dfs(grid, visited, i, j)
                maxans= max(maxans, ans)
        return maxans
