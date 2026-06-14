class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        next_free = 0
        next_holding = 0
        next_cooldown = 0
        
        for i in range(len(prices) - 1, -1, -1):
            # If holding, you can sell or wait for next day
            cur_holding = max(next_cooldown + prices[i], next_holding)

            # If on cooldown, you need to wait for next day
            cur_cooldown = next_free
            
            # If free, you can buy or wait for next day
            cur_free = max(next_holding - prices[i], next_free)

            next_free, next_holding, next_cooldown = cur_free, cur_holding, cur_cooldown
        
        return next_free