class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        count = 0

        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            # if they overlap
            if intervals[i][0] < prevEnd:
                prevEnd = min(prevEnd, intervals[i][1])
                count += 1
            else:
                prevEnd = intervals[i][1]
        
        return count 