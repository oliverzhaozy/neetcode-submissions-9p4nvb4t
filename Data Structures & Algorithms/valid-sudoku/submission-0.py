class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_visit, col_visit = set(), set()
        nums = [str(i) for i in range(1, 10)]

        # Check row for duplicates
        for r in range(9):
            for c in range(9):
                if board[r][c] in row_visit:
                    return False
                if board[r][c] in nums: row_visit.add(board[r][c])
            row_visit.clear()
        
        # Check col for duplicates
        for r in range(9):
            for c in range(9):
                if board[c][r] in col_visit:
                    return False
                if board[c][r] in nums: col_visit.add(board[c][r])
            col_visit.clear()
        
        # Check sub-box for duplicates
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                box_id = (r // 3, c // 3)
                if val in boxes[box_id]:
                    return False
                if val in nums: boxes[box_id].add(val)

        return True