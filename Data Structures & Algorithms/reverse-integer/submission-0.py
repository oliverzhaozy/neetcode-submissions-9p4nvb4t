class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_x = int(str(abs(x))[::-1])
        res = sign * reversed_x
        return res if (-(2**31) <= res <= 2**31 - 1) else 0