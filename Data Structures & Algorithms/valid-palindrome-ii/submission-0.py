class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        ans, c1, c2 = self.func(s)
        if ans:
            return ans
        return (self.func(s[0:c1]+s[c1+1:n])[0] or self.func(s[0:c2]+s[c2+1:n])[0])
        


    def func(self, s: str):
        l, r = 0, len(s)-1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return [False, l, r]

            l+=1
            r-=1
        return [True, l, r]