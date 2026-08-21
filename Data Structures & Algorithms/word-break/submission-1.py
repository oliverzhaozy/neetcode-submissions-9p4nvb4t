class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(i, cache):
            # Base case
            if i >= len(s):
                return True
            if i in cache:
                return cache[i]
            
            for word in wordDict:
                if s[i : i + len(word)] == word:
                    if dp(i + len(word), cache):
                        cache[i] = True
                        return True
            cache[i] = False
            return False
            
        return dp(0, {})