class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        cache = {}

        def dp(i):
            if i >= len(s):
                return [""]
            if i in cache:
                return cache[i]
            
            res = []
            for end in range(i, len(s)):
                word = s[i:end + 1]

                if word in wordSet:
                    for sub in dp(end + 1):
                        sentence = (word + " " + sub).strip()
                        res.append(sentence)
            cache[i] = res
            return res
        
        return dp(0)