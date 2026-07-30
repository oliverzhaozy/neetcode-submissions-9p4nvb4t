class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = defaultdict(int)
        maxFreq = 0

        for t in tasks:
            freqMap[t] += 1
            maxFreq = max(freqMap[t], maxFreq)
        
        x = 0
        for t in freqMap:
            if freqMap[t] == maxFreq:
                x += 1

        floor = (maxFreq - 1) * n + maxFreq + x - 1
        return max(floor, len(tasks))