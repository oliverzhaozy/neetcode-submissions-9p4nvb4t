class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1

            total = bit_a + bit_b + carry
            res |= (total & 1) << i
            carry = 1 if total >= 2 else 0

        if res & (1 << 31):
            res -= 1 << 32
        
        return res
