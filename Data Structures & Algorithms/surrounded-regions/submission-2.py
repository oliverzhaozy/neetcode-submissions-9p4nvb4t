class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        visit = set()
        
        # Append border cells to the queue
        for row in range(ROWS):
            if board[row][0] == "O":
                queue.append((row, 0))
                visit.add((row, 0))
            if board[row][COLS - 1] == "O":
                queue.append((row, COLS - 1))
                visit.add((row, COLS - 1))
        
        for col in range(COLS):
            if board[0][col] == "O":
                queue.append((0, col))
                visit.add((0, col))
            if board[ROWS - 1][col] == "O":
                queue.append((ROWS - 1, col))
                visit.add((ROWS - 1, col))

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and (nr, nc) not in visit and board[nr][nc] == "O":
                    visit.add((nr, nc))
                    queue.append((nr, nc))
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "O" and (row, col) not in visit:
                    board[row][col] = "X"

        return 

