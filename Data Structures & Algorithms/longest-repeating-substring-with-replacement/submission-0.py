class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        length, max_length = 0, 0
        hashmap = {}

        for _ in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            length = r - l + 1

            if length - max(hashmap.values()) > k:
                hashmap[s[l]] -= 1
                l += 1
                length -= 1
            max_length = max(max_length, length)
            r += 1

        return max_length

