class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        times_s = {}
        ans = []
        #for i,s in enumerate(strs):
        for s in strs:
            times = tuple(sorted(s))
            if times in times_s.keys():
                times_s[times].append(s)
            else:
                times_s[times] = [s]
        for value in times_s.values():
            ans.append(value)
        return ans

        