class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        names = path.split("/")
        for name in names:
            if name =='..':
                if stack:
                    stack.pop()
            elif name and name != '.':
                stack.append(name)
            
        return "/"+"/".join(stack)