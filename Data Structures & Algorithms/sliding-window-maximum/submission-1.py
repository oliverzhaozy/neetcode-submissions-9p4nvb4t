class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []

        curMax = float("-inf")
        for i in range(k):
            curMax = max(curMax, nums[i])
            heapq.heappush(maxHeap, (-nums[i], i))
        res.append(curMax)
        
        for i in range(k, len(nums)):
            heapq.heappush(maxHeap, (-nums[i], i))
            while maxHeap[0][1] < i - k + 1:
                heapq.heappop(maxHeap)
             
            res.append(-maxHeap[0][0])
        
        return res
