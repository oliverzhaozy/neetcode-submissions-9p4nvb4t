class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a): # make sure a is the longer str
            a, b = b, a
        
        carry, j = 0, len(b) - 1
        res = ""
        for i in range(len(a) - 1, -1, -1):
            a_val = int(a[i])
            b_val = int(b[j]) if j >= 0 else 0
            sum = a_val + b_val + carry

            if sum >= 2:
                carry = 1
                sum -= 2
            else:
                carry = 0
            
            j -= 1
            res += str(sum)
        
        if carry == 1:
            res += '1'
            
        return res[::-1]