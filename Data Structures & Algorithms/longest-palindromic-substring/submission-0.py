class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <2:
            return s
        dp = [[False]*n for _ in range(n)]
        begin, max_len = 0, 1
        for i in range(n-1,-1,-1):
            dp[i][i]=True
            for j in range(i+1,n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        cur_len = j-i+1
                        if cur_len >max_len:
                            begin, max_len = i, cur_len          
        return s[begin:begin+max_len]
                
                