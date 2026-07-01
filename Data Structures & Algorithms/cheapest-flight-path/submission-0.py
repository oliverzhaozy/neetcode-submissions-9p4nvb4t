class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for i in range(0, n):
            adj[i] = []
        
        for FROM, TO, price in flights:
            adj[FROM].append((TO, price))
        
        visit = set()
        minHeap = [(0, src, k)]
        remaining_stops = k 
        while minHeap:
            w1, n1, remaining_stops = heapq.heappop(minHeap)
            if n1 == dst:
                return w1
            if (n1, remaining_stops) in visit:
                continue
            visit.add((n1, remaining_stops))

            for n2, w2 in adj[n1]:
                if remaining_stops >= 0 and (n2, remaining_stops - 1) not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2, remaining_stops - 1))
        return -1