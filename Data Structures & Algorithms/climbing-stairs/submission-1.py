class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, cache):
            # Base case
            if n <= 2:
                return n
            if n in cache:
                return cache[n]
            
            cache[n] = dp(n - 1, cache) + dp(n - 2, cache)
            return cache[n]

        return dp(n, {})