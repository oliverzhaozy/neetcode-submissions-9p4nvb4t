class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxFreq, res = 0, 0
        freq_map = {}

        for r in range(len(s)):
            freq_map[s[r]] = freq_map.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq_map[s[r]])

            while (r - l + 1) - maxFreq > k: # window is invalid
                freq_map[s[l]] -= 1
                l += 1
            
            length = r - l + 1
            res = max(res, length)
        
        return res