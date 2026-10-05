class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dp(i, holding):
            # Base case
            if i >= len(prices):
                return 0
            if (i, holding) in cache:
                return cache[(i, holding)]
            
            maxProfit = 0 
            # if not holding, can buy or skip
            if not holding:
                maxProfit = max(dp(i + 1, True) - prices[i], dp(i + 1, False))
            else: # if holding, can sell or skip 
                maxProfit = max(dp(i + 1, False) + prices[i], dp(i + 1, True))
            
            cache[(i, holding)] = maxProfit
            return maxProfit
        
        return dp(0, False)
            
