class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        minHeap = []

        shortest_map = {}
        i = 0
        for q in sorted(queries):
            # while the start of interval is <= q, q is within the range 
            while i < len(intervals) and intervals[i][0] <= q:
                length = intervals[i][1] - intervals[i][0] + 1
                heapq.heappush(minHeap, (length, intervals[i]))
                i += 1
            
            # while the end of interval is < q, q is no longer in the range 
            while minHeap and minHeap[0][1][1] < q:
                heapq.heappop(minHeap)
            
            if minHeap:
                shortest_map[q] = minHeap[0][0]
            else:
                shortest_map[q] = -1
        
        # build the res in the orginal order of queries
        res = []
        for q in queries:
            res.append(shortest_map[q])
        return res