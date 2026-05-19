class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calDays(cap):
            ans, total = 1, 0
            for w in weights:
                if total + w <= cap:
                    total+=w
                else:
                    ans +=1
                    total = w
            return ans

        l, r = max(weights), sum(weights)
        while l <= r:
            m = (l+r)//2
            if calDays(m)>days:
                l = m+1
            else:
                r = m-1

        return l