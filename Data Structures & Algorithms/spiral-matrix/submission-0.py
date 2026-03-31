class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n = len(matrix), len(matrix[0])
        top, left, bottom, right = 0, 0, m-1, n-1
        res = []
        while left <= right and top <= bottom:
            for col in range(left,right+1):
                res.append(matrix[top][col])
            for row in range(top+1,bottom+1):
                res.append(matrix[row][right])
            
            if left < right and top < bottom:
                #代表如果正好left = right 或 top =bottom:只要遍历一次
                for col in range(right-1,left,-1):
                    res.append(matrix[bottom][col])
                for row in range(bottom,top,-1):
                    res.append(matrix[row][left])

            top+=1
            left+=1
            bottom-=1
            right-=1
        
        return res
