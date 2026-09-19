class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        maxHeap = []
        for n in freq_map:
            heapq.heappush(maxHeap, (-freq_map[n], n))
        
        res = []
        while k > 0:   
            res.append(heapq.heappop(maxHeap)[1])
            k -= 1
        
        return res