import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest_pile = max(piles)
        lower_bound, upper_bound = 1, biggest_pile
        min_k = biggest_pile
        
        while lower_bound <= upper_bound:
            time = 0
            k = (lower_bound + upper_bound) // 2

            for pile in piles:
                time += math.ceil(pile / k)
            
            if time > h:
                lower_bound = k + 1
            else: # time <= h
                upper_bound = k - 1
                min_k = min(k, min_k)

        return min_k