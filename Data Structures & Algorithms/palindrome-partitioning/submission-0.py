class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        def is_palindrome(s, start, end):
            i,j = start, end
            while i < j:
                if s[i] !=s[j]:
                    return False
                i+=1
                j-=1
            return True

        def backtracking(path,res,startindex):
            nonlocal n, s
            if startindex == n:
                res.append(path[:])
                return
            
            for i in range(startindex,n):
                if is_palindrome(s,startindex,i):
                    path.append(s[startindex:i+1])
                    backtracking(path, res, i+1)
                    path.pop()
        backtracking([],res,0)
        return res