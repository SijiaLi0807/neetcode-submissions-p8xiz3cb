class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = [intervals[0]]
        cur = 1
        while cur<len(intervals):
            if intervals[cur][0] > ans[-1][1]:
                ans.append(intervals[cur])
            else:
                new = [min(ans[-1][0],intervals[cur][0]),max(ans[-1][1],intervals[cur][1])]
                ans.pop()
                ans.append(new)
            cur += 1
        return ans
        