class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
                return False

        def dp(i1, i2, cache):
            # Base case
            if i1 == len(s1) and i2 == len(s2):
                return True
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            
            pathA = dp(i1 + 1, i2, cache) if (i1 < len(s1) and s1[i1] == s3[i1 + i2]) else False
            pathB = dp(i1, i2 + 1, cache) if (i2 < len(s2) and s2[i2] == s3[i1 + i2]) else False
            cache[(i1, i2)] = pathA or pathB
            return cache[(i1, i2)]
        
        return dp(0, 0, {})