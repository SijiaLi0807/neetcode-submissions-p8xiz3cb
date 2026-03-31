class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        times_s = Counter(s)
        times_t = Counter(t) 
        if times_s == times_t:
            return True
        else:
            return False
        