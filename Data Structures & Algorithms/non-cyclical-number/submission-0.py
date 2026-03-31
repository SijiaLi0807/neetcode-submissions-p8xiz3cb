class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        ans = 0
        while n !=1: 
            ans = 0
            while n:
                ans += (n%10)**2
                n = n//10
            if ans in seen:
                return False
            else:
                seen.add(ans)
            n = ans
        return True


        