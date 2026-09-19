class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l = r = 0
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        while r < len(s):
            while s[r] in numbers:
                r += 1
            length = int(s[l:r])
            l = r + 1
            r += length +1
            res.append(s[l:r])
            l = r
        return res

