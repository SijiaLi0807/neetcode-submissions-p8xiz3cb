class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        n, m = len(heights), len(heights[0])
        #firstborder = []
        #secondborder = []
        firstborder = set()
        secondborder = set()
        d = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(heights,visited,x,y,side):
            #for i in range(n)
            if visited[x][y]:
                return
            visited[x][y]=True
            #side.append([x,y])
            side.add((x,y))
            for i,j in d:
                nextx,nexty = x+i,y+j
                if -1<nextx <n and -1<nexty<m:
                    if heights[nextx][nexty]>=heights[x][y]:
                        dfs(heights,visited,nextx,nexty,side)
        visited = [[False]* m for _ in range(n)]
        for i in range(n):
            dfs(heights,visited,i,0,firstborder)
        for j in range(m):
            dfs(heights,visited,0,j,firstborder)

        visited = [[False]* m for _ in range(n)]
        for i in range(n):
            dfs(heights,visited,i,m-1,secondborder)
        for j in range(m):
            dfs(heights,visited,n-1,j,secondborder)
        #ans = [p for p in firstborder if p in secondborder]
        ans = [ list(p) for p in firstborder & secondborder]
        return ans