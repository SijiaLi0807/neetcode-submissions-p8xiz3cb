class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxval = 0
        n = len(s)
        #if n == 0:
        for i in range(n):
            seen = set()
            seen.add(s[i])
            tmp = 1
            for j in range(i+1,n):
            #while i<=j
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    tmp +=1
            maxval = max(maxval,tmp)
        return maxval

        