class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # Sort the array
        hand.sort()

        # Build a freq hash map
        count = defaultdict(int)
        for n in hand:
            count[n] += 1

        # Build a min heap
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            # Loop -- pulling smallest val, attempt to form a group of groupSize consecutive values
            start = minHeap[0]
            for i in range(groupSize):
                # Decrement count
                count[start + i] -= 1
                
                # Pop from min heap once freq == 0
                if count[start + i] == 0:
                    heapq.heappop(minHeap)
                
                # If any val is exhausted, return False immediately
                if count[start + i] < 0:
                    return False
        return True

