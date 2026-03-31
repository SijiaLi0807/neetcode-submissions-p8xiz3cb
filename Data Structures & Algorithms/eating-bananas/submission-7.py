'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s1, s2 = 1, max(piles)  
        s = s2
        while s1<=s2:
            t = 0
            s = (s1+s2)//2
            #s0 = s - 1 
            for p in piles:
                t += math.ceil(p/s)
                #t0 += math.ceil(p/s0)
            if t <= h:
                res = s
                s2 = s - 1
            else:
                s1 = s + 1
            
        return s
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
        

        