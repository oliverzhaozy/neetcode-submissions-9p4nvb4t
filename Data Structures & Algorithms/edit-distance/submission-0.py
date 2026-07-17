class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        def dp(i1, i2):
            # Base case
            if i1 == len(word1):
                return len(word2) - i2
            if i2 == len(word2):
                return len(word1) - i1
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            
            if word1[i1] == word2[i2]:
                cache[(i1, i2)] = dp(i1 + 1, i2 + 1)
                return cache[(i1, i2)]

            insert, delete, replace = 0, 0, 0
            # Choice to insert
            insert = dp(i1, i2 + 1)

            # Choice to delete
            delete = dp(i1 + 1, i2)

            # Choice to replace
            replace = dp(i1 + 1, i2 + 1)

            cache[(i1, i2)] = 1 + min(insert, delete, replace)
            return cache[(i1, i2)]
            
        return dp(0, 0)