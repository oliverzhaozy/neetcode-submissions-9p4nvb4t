class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        row_zero = False

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    if row > 0:
                        matrix[row][0] = 0
                    else:
                        row_zero = True
                    matrix[0][col] = 0
                
        for i in range(1, ROWS):
            if matrix[i][0] == 0:
                for j in range(COLS):
                    matrix[i][j] = 0
        
        for j in range(COLS):
            if matrix[0][j] == 0:
                for i in range(1, ROWS):
                    matrix[i][j] = 0

        if row_zero:
            for j in range(COLS):
                matrix[0][j] = 0