class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = float("inf")
        for s in strs:
            minLen = min(minLen, len(s))
        
        res = ""
        for i in range(minLen):
            first = strs[0][i]
            same = True
            for s in strs:
                if s[i] != first:
                    same = False
                    break
            
            if same == True:
                res += first
            else:
                break
        
        return res