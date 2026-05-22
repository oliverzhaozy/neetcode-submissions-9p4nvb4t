class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            grid[row][col] = '0'

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] == '0':
                        continue
                    grid[nr][nc] = '0'
                    queue.append((nr, nc))

        
        counter = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    bfs(row, col)
                    counter += 1
        return counter