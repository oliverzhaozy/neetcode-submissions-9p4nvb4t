class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i, cache):
            # Base case
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in cache:
                return cache[i]
            
            res = 0
            if 10 <= int(s[i:i + 2]) <= 26:
                res += dp(i + 1, cache) + dp(i + 2, cache)
            else:
                res += dp(i + 1, cache)
            
            cache[i] = res
            return res
        
        return dp(0, {})
