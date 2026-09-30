class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        res = float("inf")
        while low <= high:
            k = (low + high) // 2

            time = 0
            for p in piles:
                time += math.ceil(p / k)
                if time > h:
                    break
            
            if time <= h:
                res = min(res, k)
                high = k - 1
            else:
                low = k + 1
        
        return res