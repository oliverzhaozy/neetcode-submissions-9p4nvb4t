class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        seen = set()

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = r - l + 1
            res = max(res, length)
            r += 1
        
        return res