class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)
        ans = ""
        while i < n1 and j < n2:
            ans+=word1[i]
            i+=1
            ans+=word2[j]
            j+=1
        if i < n1:
            ans+=word1[i:n1]
        else:
            ans+=word2[j:n2]
        return ans
