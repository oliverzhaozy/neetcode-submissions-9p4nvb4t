class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        if len(s) != len(t):
            return False

        for i in s:
            letters[i] = letters.get(i, 0) + 1
        for j in t:
            letters[j] = letters.get(j, 0) - 1
        for k in letters:
            if letters[k] != 0:
                return False
        return True

        