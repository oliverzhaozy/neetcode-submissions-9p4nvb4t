class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def minCost(i, cache, steps):
            # Base case
            if i <= 1:
                return 0
            if i in cache:
                return cache[i]
            
            cache[i] = min(minCost(i - 1, cache, steps) + cost[i - 1], minCost(i - 2, cache, steps) + cost[i - 2])
            return cache[i]

        return minCost(len(cost), {}, len(cost))