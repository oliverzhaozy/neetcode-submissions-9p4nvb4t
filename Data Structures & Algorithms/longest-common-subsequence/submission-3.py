class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLS = len(text2), len(text1)
        prevRow = [0] * (COLS + 1)
        curRow = [0] * (COLS + 1)

        for i in range(ROWS - 1, -1, -1):
            for j in range(COLS - 1, -1, -1):
                if text1[j] == text2[i]:
                    curRow[j] = 1 + prevRow[j + 1]
                else:
                    curRow[j] = max(prevRow[j], curRow[j + 1])
            prevRow = curRow
            curRow = curRow.copy()
        
        return curRow[0]