class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(row, col, prev_height, visit):
            # Base case
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row, col) in visit:
                return
            if heights[row][col] < prev_height:
                return
            
            visit.add((row, col))
            dfs(row + 1, col, heights[row][col], visit)
            dfs(row - 1, col, heights[row][col], visit)
            dfs(row, col + 1, heights[row][col], visit)
            dfs(row, col - 1, heights[row][col], visit)

        for row in range(ROWS):
            dfs(row, 0, heights[row][0], pacific) # left col
            dfs(row, COLS - 1, heights[row][COLS - 1], atlantic) # right col
        
        for col in range(COLS):
            dfs(0, col, heights[0][col], pacific)
            dfs(ROWS - 1, col, heights[ROWS - 1][col], atlantic)

        res = []
        common = pacific & atlantic
        return [list(coords) for coords in common]