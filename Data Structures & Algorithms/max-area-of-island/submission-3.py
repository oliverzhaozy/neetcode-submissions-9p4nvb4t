class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def bfs(row, col):
            if grid[row][col] == 0:
                return 0

            queue = deque()
            queue.append((row, col))
            grid[row][col] = 0
            area = 1

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    grid[nr][nc] = 0
                    area += 1
                    queue.append((nr, nc))
            return area
        
        max_area = 0
        for row in range(ROWS):
            for col in range(COLS):
                max_area = max(bfs(row, col), max_area)
        return max_area
