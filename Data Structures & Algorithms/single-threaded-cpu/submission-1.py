class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, task in enumerate(tasks):
            task.append(i) # task: [enqueueTime, processingTime, originalIndex]
        tasks.sort(key=lambda x:x[0])
        i, time = 0, 1
        minHeap, res = [], []

        while len(res) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(minHeap, (tasks[i][1], tasks[i][2])) # (processingTime, originalIndex)
                i += 1
            
            if minHeap:
                processingTime, j = heapq.heappop(minHeap)
                res.append(j)
                time += processingTime
            else:
                time = tasks[i][0]
        
        return res