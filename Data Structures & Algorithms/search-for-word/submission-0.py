class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, ni,nj = len(word), len(board),len(board[0])

        def check(i,j,k):  #  check if we can get the word starting at board(i,j)
            if not 0<= i < ni or not 0<= j <nj or board[i][j] != word[k]:
            #board[i][j], not board[i,j]
                return False
            if k == n-1:
                return True
            board[i][j]= None #用掉。
            # let board[i,j] = empty to make sure it will not be used again
            res = check(i+1,j,k+1) or check(i,j+1,k+1) or check(i-1,j,k+1) or check(i,j-1,k+1)
            board[i][j] = word[k] #补回去
            return res

        for i in range(ni):
            for j in range(nj):
                if check(i,j,0):
                    return True
        return False
