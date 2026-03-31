class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #reduce() 是 Python 里的一个“把一串数据折叠成一个值”的函数：
        #^: XOR
        ans = 0
        for n in nums:
            ans ^= n
        return ans
        #return reduce(lambda x, y: x ^ y, nums)