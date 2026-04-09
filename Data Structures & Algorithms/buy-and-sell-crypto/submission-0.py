class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = 9999
        max_profit = 0
        for price in prices:
            if price < lowest_price:
                lowest_price = price
            if price - lowest_price > max_profit:
                max_profit = price - lowest_price
        if max_profit <= 0:
            return 0
        else:
            return max_profit