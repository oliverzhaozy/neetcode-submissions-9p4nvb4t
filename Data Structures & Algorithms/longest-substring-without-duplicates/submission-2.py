class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        length, max_length = 0, 0
        hashset = set()
        
        for char in s:
            if char in hashset:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l += 1
            hashset.add(char)
            length = r - l + 1
            max_length = max(length, max_length)
            r += 1

        return max_length