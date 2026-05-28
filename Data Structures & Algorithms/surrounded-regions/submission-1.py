class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(row, col, visit):
            # Base case
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return
            if board[row][col] == "X" or (row, col) in visit:
                return 
            
            visit.add((row, col))
            dfs(row + 1, col, visit)
            dfs(row - 1, col, visit)
            dfs(row, col + 1, visit)
            dfs(row, col - 1, visit)
        
        for row in range(ROWS):
            dfs(row, 0, visit)
            dfs(row, COLS - 1, visit)
        
        for col in range(COLS):
            dfs(0, col, visit)
            dfs(ROWS - 1, col, visit)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visit:
                    board[row][col] = "X"

        return