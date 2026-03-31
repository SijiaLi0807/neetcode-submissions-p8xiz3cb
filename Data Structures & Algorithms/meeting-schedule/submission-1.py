"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i: i.start)
        ans = [intervals[0]]
        cur = 1
        while cur<len(intervals):
            if intervals[cur].start < ans[-1].end:
                return False
            else:
                ans.append(intervals[cur])
            cur += 1
        return True
