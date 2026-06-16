class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dp(i, amount, cache):
            # Base case
            if i >= len(coins) or amount < 0:
                return 0
            if amount == 0:
                return 1
            if (i, amount) in cache:
                return cache[(i, amount)]
            
            count = 0
            # Choice to not include ith coin
            count += dp(i + 1, amount, cache)
            
            # Choice to include ith coin
            new_amount = amount - coins[i]
            count += dp(i, new_amount, cache)
            
            cache[(i, amount)] = count
            return count

        return dp(0, amount, {})