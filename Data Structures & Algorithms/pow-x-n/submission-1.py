class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            # Base case
            if n == 0:
                return 1
            
            res = 0
            if n % 2 == 0: # n is even
                res = helper(x, n // 2)
                res *= res
            else: # n is odd
                res = helper(x, n // 2) 
                res *= res * x
            return res
        
        res = helper(x, abs(n))
        return res if n >= 0 else 1/res
