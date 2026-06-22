class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        for i in range(32):
            if n % 2 == 1:
                res += 1 
            n = n // 2
        return res