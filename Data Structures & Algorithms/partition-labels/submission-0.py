class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {} # char: last i that char appears
        for i, char in enumerate(s):
            last_pos[char] = i
        
        res = []
        l = r = 0
        cur_window_max = 0
        while r < len(s):
            cur_window_max = max(cur_window_max, last_pos[s[r]])
            if r == cur_window_max:
                res.append(r - l + 1)
                l = r + 1
            r += 1
        
        return res