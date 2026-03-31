class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        for i in range(32):
            if n == 0:
                break
            rev |= (n&1) << (31-i)
            n >>= 1
        return rev