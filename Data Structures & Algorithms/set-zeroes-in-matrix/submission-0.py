class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    continue
                for row in range(m):
                    if matrix[row][j] != 0:
                        matrix[row][j] = 'A'
                for col in range(n):
                    if matrix[i][col] !=0:
                        matrix[i][col] = 'A' 


        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'A':
                    matrix[i][j] = 0

        
        