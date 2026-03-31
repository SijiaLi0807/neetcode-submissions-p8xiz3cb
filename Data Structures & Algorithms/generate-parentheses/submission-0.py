class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = ['']*(2*n) #不是[] * 5，因为重复没有元素=没有元素
        '''
        枚举当前位置填左括号还是右括号
        本质是「选或不选」的思想，你可以把填左括号视作「选」，填右括号视作「不选」。
        '''
        def backtracking(res,path,left,right):
            nonlocal n
            
            if right==n:
                res.append("".join(path[:]))
                return
            if left < n:
                path[left+right]='('
                backtracking(res,path,left+1,right)
            if right < left:
                path[left+right]=')'
                backtracking(res,path,left,right+1)
        backtracking(res,path,0,0)
        return res