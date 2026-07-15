class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_freq = defaultdict(int)
        for char in s1:
            s1_freq[char] += 1
        
        l = r = 0
        s2_freq = defaultdict(int)
        for char in s2:
            s2_freq[char] += 1
            r += 1

            if (r - l) > len(s1):
                if s2_freq[s2[l]] == 1:
                    del s2_freq[s2[l]]
                else:
                    s2_freq[s2[l]] -= 1
                l += 1

            if s1_freq == s2_freq:
                return True
        return False