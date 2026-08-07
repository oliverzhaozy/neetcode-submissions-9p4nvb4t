class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(i, curRes):
            # Base case
            if i >= len(s):
                res.append(curRes.copy())
                return
            
            for end in range(i, len(s)):
                sub = s[i:end + 1]
                if sub == sub[::-1]:
                    curRes.append(sub)
                    backtrack(end + 1, curRes)
                    curRes.pop()
        
        backtrack(0, [])
        return res