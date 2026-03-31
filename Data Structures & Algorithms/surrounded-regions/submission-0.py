class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        m, n = len(board), len(board[0])
        directions = [[0,1], [0,-1],[1,0],[-1,0]]

        def dfs(x, y):
            '''
            change the 'o's on the edge and its neiboghood 'o's into 'a' (for protection) 
            '''
            if not 0<= x < m or not 0<= y < n or board[x][y] !='O':
                return
            board[x][y] = 'A'
            for i, j in directions:
                dfs(x+i,y+j)
        # dfs:找边界o以及与他相连的o，先变成a

        # traverse the edges to find 'O's that need to be protected. don't consider 'O' as a start point in the middle.

        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)

        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        
        # recovery: 'O'>'X', 'A'>'O'

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'