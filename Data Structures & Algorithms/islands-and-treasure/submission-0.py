class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            for j in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc] == 2147483647:
                        queue.append((nr, nc))
                        dist = grid[row][col]
                        grid[nr][nc] = dist + 1
        
        return 


