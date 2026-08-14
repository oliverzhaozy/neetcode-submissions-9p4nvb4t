class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])

        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == 0:
                    for i in range(ROWS):
                        if matrix[i][col] != 0:
                            matrix[i][col] = -1
                    for j in range(COLS):
                        if matrix[row][j] != 0:
                            matrix[row][j] = -1
        
        for row in range(ROWS):
            for col in range(COLS):
                if matrix[row][col] == -1:
                    matrix[row][col] = 0
        