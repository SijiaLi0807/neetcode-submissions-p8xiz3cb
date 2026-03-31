class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        res = []
        hash = {}
        left = right = 0
        for i in range(n):
            hash[s[i]]=i 
        for i in range(n):
            right = max(right,hash[s[i]])#s[i]-a
            if i == right:
                res.append(right-left+1)
                left = right+1
        return res