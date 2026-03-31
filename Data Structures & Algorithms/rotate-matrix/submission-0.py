class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res[j][n-i-1] = matrix[i][j]
        matrix[:] = res
        #不能写 matrix = res

        #因为 matrix = res 只是让局部变量 matrix 指向了一个新对象res
        #并没有改掉外面传进来的那个原列表。
        #而题目要求是：modify matrix in-place
        # [1,1] -> [1,4]
        # [1,2] -> [2,4]
        # [1,3] -> [3,4]
        # [2,1] -> [1,3]
        # [3,1] -> [1,2]
        # [i,j] -> [j,n-i+1]