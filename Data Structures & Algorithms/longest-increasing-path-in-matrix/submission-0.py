class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(row, col, prev_num):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return 0
            if matrix[row][col] <= prev_num:
                return 0
            if (row, col) in cache:
                return cache[(row, col)]
            
            res = 1 + max(dfs(row + 1, col, matrix[row][col]),
            dfs(row - 1, col, matrix[row][col]),
            dfs(row, col + 1, matrix[row][col]),
            dfs(row, col - 1, matrix[row][col]))

            cache[(row, col)] = res
            return res
        
        longest = 0
        for row in range(ROWS):
            for col in range(COLS):
                longest = max(longest, dfs(row, col, -1))
        
        return longest
        