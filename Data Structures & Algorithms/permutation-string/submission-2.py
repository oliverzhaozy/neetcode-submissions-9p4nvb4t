class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1

        s2_map = {}
        maxWindowLen = len(s1) 
        l = 0
        for r in range(len(s2)):
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            if (r - l + 1) > maxWindowLen:
                s2_map[s2[l]] -= 1
                if s2_map[s2[l]] == 0:
                    del s2_map[s2[l]]
                l += 1
            if s1_map == s2_map:
                return True 
        
        return False