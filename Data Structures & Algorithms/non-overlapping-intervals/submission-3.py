class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        #ans = [intervals[0]]
        preend = intervals[0][1]
        res = 0
        cur = 1
        while cur<len(intervals):
            if intervals[cur][0] >= preend:
                preend = intervals[cur][1] #???
            else:
                preend = min(preend, intervals[cur][1])
                res +=1
            cur += 1
        return res
        