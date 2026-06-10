class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        n = len(intervals)

        if n == 1:
            return [intervals[0]]

        start, end = intervals[0][0], intervals[0][1]
        for i in range(1, n):
            # If they don't overlap
            if end < intervals[i][0]:
                res.append([start, end])
                start, end = intervals[i][0], intervals[i][1]
            # If they overlap
            else:
                end = max(end, intervals[i][1])
        res.append([start, end])
        return res

