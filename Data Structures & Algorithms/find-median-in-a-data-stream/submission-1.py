class MedianFinder:

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        if self.maxHeap and num >= -self.maxHeap[0]: # meaning the num should belong to the larger heap
            heapq.heappush(self.minHeap, num)
        elif self.minHeap and num < self.minHeap[0]: # meaning the num should belong to the smaller heap
            heapq.heappush(self.maxHeap, -num)
        else: # self.minHeap and self.maxHeap are empty
            heapq.heappush(self.maxHeap, -num)

        # if size of 1 heap is larger than the other by more than 1, rebalance the elements 
        if len(self.maxHeap) > len(self.minHeap) + 1:
            temp = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, temp)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            temp = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -temp)

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap): # median belongs to minHeap
            return float(self.minHeap[0])
        elif len(self.maxHeap) > len(self.minHeap): # median belongs to maxHeap
            return float(-self.maxHeap[0])
        else: # both heaps are the same size
            return float((self.minHeap[0] - self.maxHeap[0]) / 2.0)

        
        