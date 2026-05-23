class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(row, col):
            # Base case
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            neighbour_area = 1
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                neighbour_area += dfs(nr, nc)
            return neighbour_area

        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(dfs(row, col), max_area)

        return max_area