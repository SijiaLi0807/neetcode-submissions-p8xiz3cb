class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r, n = 1, max(piles), len(piles) 
        while l < r:
            mid = (l + r) // 2
            if sum((p-1)//mid for p in piles) <= h-n:
                ##不用ceil的话，可直接用整除: (p+mid-1)//mid=(p-1)//mid+1。
                r = mid
            else:
                l = mid + 1    # 关键：l+1，r不加一，因为l永远不行，r行 
        return r #r和l都行，因为最后两者相等

        