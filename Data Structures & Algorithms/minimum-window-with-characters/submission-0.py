class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = r = 0
        target, window = {}, {}
        for char in t:
            target[char] = target.get(char, 0) + 1
            window[char] = window.get(char, 0)
        have, need = 0, len(target)
        
        res = ""
        while r < len(s):
            if s[r] in target:
                window[s[r]] += 1
                if window[s[r]] == target[s[r]]:
                    have += 1

            while have == need:
                if not res: # if res is empty, update res
                    res = s[l:r + 1]
                else: # if new res is shorter, update res
                    if len(s[l: r + 1]) < len(res):
                        res = s[l: r + 1]
                        
                if s[l] in window:
                    window[s[l]] -= 1
                    if window[s[l]] < target[s[l]]:
                        have -= 1
                l += 1
            r += 1
        return res
                
                
         
            