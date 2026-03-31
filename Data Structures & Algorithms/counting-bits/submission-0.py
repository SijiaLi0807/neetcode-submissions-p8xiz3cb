class Solution:
    def countBits(self, n: int) -> List[int]:
                #可用动态规划改进
        #https://leetcode.cn/problems/counting-bits/solutions/627418/bi-te-wei-ji-shu-by-leetcode-solution-0t1i
        ans = [0]
        for i in range(1,n+1):
            n = 0
            while i:
                i &= (i-1)
                n +=1
            ans.append(n)
        return ans

