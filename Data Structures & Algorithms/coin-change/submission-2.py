class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float("inf")] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][amount] = 0

        for i in range(n - 1, -1, -1):
            for j in range(amount - 1, -1, -1):
                if j + coins[i] <= amount:
                    dp[i][j] = min(1 + dp[i][j + coins[i]], dp[i + 1][j])
                else:
                    dp[i][j] = dp[i + 1][j]
        
        res = dp[0][0]
        return res if res != float("inf") else -1