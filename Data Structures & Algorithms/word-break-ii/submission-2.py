class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        wordSet = set(wordDict)

        dp = [[] for _ in range(n + 1)]
        dp[n] = [""]
        
        for i in range(n - 1, -1, -1):
            for end in range(i, n):
                word = s[i:end + 1]

                if word in wordSet:
                    for sub in dp[end + 1]:
                        sentence = (word + " " + sub).strip()
                        dp[i].append(sentence)
        
        return dp[0]