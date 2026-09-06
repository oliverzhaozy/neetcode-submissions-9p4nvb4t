class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dp(i, j, cache):
            # Base case
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if (i, j) in cache:
                return cache[(i, j)]
            
            first_match = (i < len(s) and (s[i] == p[j] or p[j] == '.'))
            if j + 1 < len(p) and p[j + 1] == '*':
                res = dp(i, j + 2, cache) or (first_match and dp(i + 1, j, cache))
            else:
                res = first_match and dp(i + 1, j + 1, cache)
            
            cache[(i, j)] = res
            return res
        
        return dp(0, 0, {})
