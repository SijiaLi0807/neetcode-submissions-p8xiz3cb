class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = []
        count = 0 # fresh orange
        d = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(m):
            for c in range(n):
                if not grid[r][c]:
                    continue
                if grid[r][c] ==1:
                    count+=1
                else:
                    queue.append((r,c))

        mins = 0 
        while count and queue:
            mins +=1
            N = len(queue)
            for i in range(N):
                r,c = queue.pop(0)
                for x,y in d:
                    nextr, nextc = r+x, c+y
                    if nextr < 0 or nextr>= m or nextc< 0 or nextc >= n:
                        continue   
                    if grid[nextr][nextc] == 1:            
                        grid[nextr][nextc] = 2
                        count -=1
                        queue.append((nextr,nextc))
        
        if count:
            return -1
        return mins


