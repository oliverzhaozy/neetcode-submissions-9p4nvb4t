class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [0] * n
        trusts = [0] * n

        for a, b in trust: # a trusts b:
            trusted_by[b - 1] += 1
            trusts[a - 1] += 1
        
        for i in range(n):
            if trusts[i] == 0 and trusted_by[i] == (n - 1):
                return i + 1
        return -1