class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
                return False
        
        nextRow = [False] * (len(s2) + 1)
        nextRow[len(s2)] = True
        for i2 in range(len(s2) - 1, -1, -1):
            nextRow[i2] = nextRow[i2 + 1] and s2[i2] == s3[len(s1) + i2]
 
        for i1 in range(len(s1) - 1, -1, -1):
            curRow = [False] * (len(s2) + 1)

            for i2 in range(len(s2), -1, -1):
                pathA = nextRow[i2] if (i1 < len(s1) and s1[i1] == s3[i1 + i2]) else False
                pathB = curRow[i2 + 1] if (i2 < len(s2) and s2[i2] == s3[i1 + i2]) else False
                curRow[i2] = pathA or pathB
            
            nextRow = curRow
        
        return nextRow[0]