class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(nums):
            res = 0
            while nums:
                num = nums % 10
                res += num ** 2
                nums //= 10
            return res

        seen = set()
        while n not in seen:
            seen.add(n)
            n = helper(n)
            if n == 1:
                return True
        return False
