"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()

        count = res = 0
        i = j = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(count, res)
        return res

