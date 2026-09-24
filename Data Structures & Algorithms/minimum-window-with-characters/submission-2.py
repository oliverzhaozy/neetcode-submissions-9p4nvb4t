class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        freq_map = {}
        for char in t:
            freq_map[char] = freq_map.get(char, 0) + 1
        
        l, r = 0, 0
        need, have = len(freq_map), 0
        cur_map = {}
        res = ""
        while r < len(s):
            if s[r] in freq_map:
                cur_map[s[r]] = cur_map.get(s[r], 0) + 1
                if cur_map[s[r]] == freq_map[s[r]]:
                    have += 1
                
                while have == need:
                    while s[l] not in freq_map:
                        l += 1
                    
                    if not res:
                        res = s[l:r + 1]
                    if len(s[l:r + 1]) < len(res):
                        res = s[l:r + 1]
                    
                    cur_map[s[l]] -= 1
                    if cur_map[s[l]] < freq_map[s[l]]:
                        have -= 1
                    l += 1
            r += 1
        
        return res