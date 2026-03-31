class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1 
        while l<r:
            while l<r and not s[l].isalnum(): #用while而不用if，因为可能不止跳过一次
                l +=1
            while l<r and not s[r].isalnum():
                r -=1
            if s[l].lower() != s[r].lower():
                return False  
            l +=1
            r -=1 
        return True

              
        