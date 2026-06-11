class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dp(row, col, cache):
            # Base case
            if row < 0 or col < 0 or row >= m or col >= n:
                return 0
            if row == m - 1 and col == n - 1:
                return 1
            if (row, col) in cache:
                return cache[(row, col)]
            
            count = 0
            count += dp(row + 1, col, cache)
            count += dp(row, col + 1, cache)
            cache[(row, col)] = count
            return count
        
        return dp(0, 0, {})
