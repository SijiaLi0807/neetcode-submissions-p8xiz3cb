class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        times = dict()
        n = len(s)
        maxlen, l, r = 0, 0, 0
        while r < n:
            if s[r] in times:
                times[s[r]] +=1
            else:
                times[s[r]] = 1
            maxlen = max(maxlen,times[s[r]])#只可能是新加入的这个字母大于原maxn
            if r - l - maxlen >= k: #左指针右移
                times[s[l]] -=1
                l +=1
            r +=1
        return r - l

        