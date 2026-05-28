class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(row, col, hashset):
            # Base case
            if row < 0 or col < 0 or row >= ROWS or col >= COLS:
                return
            if board[row][col] == "X" or (row, col) in hashset:
                return

            hashset.add((row, col))
            dfs(row + 1, col, hashset)
            dfs(row - 1, col, hashset)
            dfs(row, col + 1, hashset)
            dfs(row, col - 1, hashset)
        
        for row in range(ROWS):
            if board[row][0] == "O":
                dfs(row, 0, visit)
            if board[row][COLS - 1] == "O":
                dfs(row, COLS - 1, visit)


        for col in range(COLS):
            if board[0][col] == "O":
                dfs(0, col, visit)
            if board[ROWS - 1][col] == "O":
                dfs(ROWS - 1, col, visit)

        
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in visit:
                    board[row][col] = "X"
        
        return
