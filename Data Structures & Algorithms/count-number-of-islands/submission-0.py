class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        counter = 0

        def sink_island(row, col):
            # Base case
            if int(row) < 0 or int(col) < 0 or row == ROWS or col == COLS:
                return
            if grid[row][col] == '0':
                return
            
            grid[row][col] = '0'
            sink_island(row + 1, col)
            sink_island(row - 1, col)
            sink_island(row, col + 1)
            sink_island(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1':
                    counter += 1
                    sink_island(row, col)
        return counter
        


        