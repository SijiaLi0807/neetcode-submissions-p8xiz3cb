class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in range(len(matrix)):
            c = 0
            #for c in range(matrix[0]):
            while matrix[r][c] < target and c < len(matrix[0])-1:
                    c +=1
            if matrix[r][c] ==target:
                return True
            elif matrix[r][c] > target:
                break
        return False
            

        
        