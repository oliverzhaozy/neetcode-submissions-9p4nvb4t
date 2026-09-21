class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        l, r = 1, x
        res = 1
        while l <= r:
            m = (l + r) // 2
            if m * m <= x:
                l = m + 1
                res = max(res, m)
            else:
                r = m - 1
        
        return res