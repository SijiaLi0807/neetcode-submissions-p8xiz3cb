class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i =='{':
                stack.append('}')
            elif i =='(':
                stack.append(')')
            elif i =='[':
                stack.append(']')
            elif not stack or stack[-1] !=i: #后进先出
                return False
            else:
                stack.pop()
        return False if stack else True
        