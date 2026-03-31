class Solution:
    def myPow(self, x: float, n: int) -> float:
        def traversal(x,i):
            if i == 0:
                return 1
            y = traversal(x,i//2)
            return y * y * x**(i%2)
        if n >= 0:
            return traversal(x,n)
        else:
            return 1/traversal(x,-n) #注意n小于0的情况