class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left = left >> 1 # >>右移（向下整除2）
            right = right >> 1
            shift+=1
        return right<<shift 
        # left << shift也行
        # <<左移（乘以2）