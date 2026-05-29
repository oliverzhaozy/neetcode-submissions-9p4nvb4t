class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            # Check boundaries and if the cell is an 'O'
            if (row < 0 or col < 0 or row >= ROWS or 
                col >= COLS or board[row][col] != "O"):
                return
            
            # Mark the 'O' as 'Safe' by changing it to a temporary character
            board[row][col] = "T"
            
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        # 1. Capture unsurrounded regions (border 'O's)
        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        
        # 2. Capture surrounded regions ('O' -> 'X')
        # 3. Uncapture unsurrounded regions ('T' -> 'O')
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"