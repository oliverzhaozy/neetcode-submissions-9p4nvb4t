class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1]) # sort by from 
        minHeap = [] # to[i], numPassengers[i]
        disp = 0 # disp = displacement from initial location
        curCap = 0

        for i in range(len(trips)):
            heapq.heappush(minHeap, (trips[i][2], trips[i][0]))
            curCap += trips[i][0]

            while disp >= minHeap[0][0]:
                to, numPassengers = heapq.heappop(minHeap)
                curCap -= numPassengers
            
            if curCap > capacity:
                return False
            
            if (i + 1) < len(trips):
                disp = trips[i + 1][1] # skip disp to next trip's from 
        
        return True