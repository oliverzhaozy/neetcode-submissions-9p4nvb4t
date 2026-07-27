class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dp(i, curSum):
            # Base case
            if curSum > amount:
                return float("inf")
            if i >= len(coins):
                return float("inf")                
            if curSum == amount:
                return 0
            if (i, curSum) in cache:
                return cache[(i, curSum)]
            
            cache[(i, curSum)] = min(1 + dp(i, curSum + coins[i]), dp(i + 1, curSum))
            return cache[(i, curSum)]

        res = dp(0, 0)
        return res if res != float("inf") else -1