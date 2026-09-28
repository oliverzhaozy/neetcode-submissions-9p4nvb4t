class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        res = []

        def dp(start, end, curRes): 
            # Base case
            if start >= len(s):
                res.append(curRes.strip())
                return
            if end >= len(s):
                return
            
            if s[start:end + 1] in wordSet:
                # Choice to include start[i]
                dp(end + 1, end + 1, curRes + (" " if curRes else "") + s[start:end + 1])

            # Choice to exclude start[i]
            dp(start, end + 1, curRes)
        
        dp(0, 0, "")
        return res