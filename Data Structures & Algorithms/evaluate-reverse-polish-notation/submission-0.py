class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(y+x)
            elif t == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif t == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))#注意python中负数除法的表现与题目不一致
            elif t == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(y*x)
            else:
                stack.append(int(t))
        return stack[0]