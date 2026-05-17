class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Store distance and coordinates in a tuple
        data = []
        for x, y in points:
            dist_sq = x**2 + y**2
            data.append((dist_sq, [x, y]))

        # Maintain a max heap of size k
        max_heap = [(-dist, coords) for dist, coords in data]
        heapq.heapify(max_heap)

        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        res = [coords for dist, coords in max_heap]
        return res