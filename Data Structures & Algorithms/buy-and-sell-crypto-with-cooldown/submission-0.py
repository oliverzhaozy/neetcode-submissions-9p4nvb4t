class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dp(i, state, cache):
            # Base case
            if i >= len(prices):
                return 0
            if (i, state) in cache:
                return cache[(i, state)]
            
            # If holding, you can sell or wait for next day
            if state == "holding":
                cache[(i, "holding")] = max(dp(i + 1, "cooldown", cache) + prices[i], dp(i + 1, "holding", cache))
                return cache[(i, state)]

            # If on cooldown, you need to wait for next day
            if state == "cooldown":
                return dp(i + 1, "free", cache)

            # If free, you can buy or wait for next day
            if state == "free":
                cache[(i, "free")] = max(dp(i + 1, "holding", cache) - prices[i], dp(i + 1, "free", cache))
                return cache[(i, state)]
            
        return dp(0, "free", {})