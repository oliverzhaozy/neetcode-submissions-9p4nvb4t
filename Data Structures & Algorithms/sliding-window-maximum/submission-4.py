class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap, res = [], []
        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))
        res.append(-maxHeap[0][0])
        
        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            
            while maxHeap[0][1] <= (i - k):
                heapq.heappop(maxHeap)
            res.append(-maxHeap[0][0])
        
        return res