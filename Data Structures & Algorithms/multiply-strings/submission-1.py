class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = [0] * (len(num1) + len(num2))
        rev1, rev2 = num1[::-1], num2[::-1]

        for i in range(len(rev2)):
            for j in range(len(rev1)):
                product = int(rev2[i]) * int(rev1[j])
                pos = i + j
                total = res[pos] + product
                res[pos] = total % 10
                res[pos + 1] += total // 10
        
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return "".join(str(d) for d in res[::-1])