class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = set(), set(), defaultdict(set)

        for r in range(9):
            row.clear()
            for c in range(9):
                if board[r][c] in row:
                    return False
                if board[r][c] != ".":
                    row.add(board[r][c]) 
        
        for c in range(9):
            col.clear()
            for r in range(9):
                if board[r][c] in col:
                    return False
                if board[r][c] != ".":
                    col.add(board[r][c])
        
        for r in range(9):
            for c in range(9):
                key = (r // 3, c // 3)
                if board[r][c] in box[key]:
                    return False
                if board[r][c] != ".":
                    box[key].add(board[r][c])
        
        return True