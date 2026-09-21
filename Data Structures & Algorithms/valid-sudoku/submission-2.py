class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, col, box = defaultdict(set), defaultdict(set), defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                box_id = (r // 3, c // 3)
                num = board[r][c]
                if num in row[r] or num in col[c] or num in box[box_id]:
                    return False
                if num != ".":
                    row[r].add(num)
                    col[c].add(num)
                    box[box_id].add(num)
        
        return True