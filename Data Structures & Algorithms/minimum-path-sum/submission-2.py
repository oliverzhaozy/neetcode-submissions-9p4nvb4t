class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cache = {}

        def dfs(r, c, curSum):
            # Base case
            if r >= m or c >= n:
                return float("inf")
            if (r, c) == (m - 1, n - 1):
                return curSum + grid[r][c]
            if (r, c, curSum) in cache:
                return cache[(r, c, curSum)]
            
            res = min(dfs(r + 1, c, curSum + grid[r][c]), dfs(r, c + 1, curSum + grid[r][c]))
            cache[(r, c, curSum)] = res
            return res

        return dfs(0, 0, 0)