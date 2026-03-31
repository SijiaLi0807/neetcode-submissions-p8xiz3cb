class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        newboard = []
        n = len(board[0])
        for r in range(len(board)):
            freq_r = Counter(board[r])
            freq_r["."] = 0
            if any(value >1 for value in freq_r.values()):
                return False
            for i in range(n):
                if r:
                    newboard[i].append(board[r][i])
                else:
                    newboard.append(list(board[r][i]))
        for r in newboard:
            freq_r = Counter(r)
            freq_r["."] = 0
            if any(value > 1 for value in freq_r.values()):
                return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                tmplist = [board[i][j],board[i+1][j],board[i+2][j],
                board[i][j+1],board[i+1][j+1],board[i+2][j+1],
                board[i][j+2],board[i+1][j+2],board[i+2][j+2]
                ]
                freq_r = Counter(tmplist)
                freq_r["."] = 0
                if any(value > 1 for value in freq_r.values()):
                    return False
        return True
          
        