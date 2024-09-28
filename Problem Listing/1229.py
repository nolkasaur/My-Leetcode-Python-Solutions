# https://leetcode.com/problems/meeting-scheduler/
# I don't have leetcode premium

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        curr = 0
        intervals.sort(key = lambda x : x.start)
        for i in range(len(intervals)-1):
            if intervals[i+1].start < intervals[i].end:
                return False
        return True
