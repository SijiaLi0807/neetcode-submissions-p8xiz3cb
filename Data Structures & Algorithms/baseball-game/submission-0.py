class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ans = 0
        for o in operations:
            if o =='+':
                stack.append(stack[-1]+stack[-2])
            elif o =='D':
                stack.append(2*stack[-1])
            elif o == 'C':
                stack.pop()
            else:
                stack.append(int(o))
        for n in stack:
            ans+=n
        return ans
        
            
