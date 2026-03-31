class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        times_s = Counter(s)
        times_t = Counter(t) 
        if times_s == times_t:
            return True
        else:
            return False
        '''

        times_s, times_t = {}, {}
        for cap in s:
            if cap in times_s.keys(): 
                times_s[cap] +=1
            else:
                times_s[cap] = 1
        for cap in t:
            if cap in times_t.keys(): 
                times_t[cap] +=1
            else:
                times_t[cap] = 1

        if times_s == times_t:
            return True
        else:
            return False
            

