class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        # Sort the array
        hand.sort()

        # Build a freq hash map
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # Build a min heap
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            start = minHeap[0]
            for i in range(start, start + groupSize):
                if i not in count:
                    return False

                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True