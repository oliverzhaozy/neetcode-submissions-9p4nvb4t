class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n - 1
        t, b = 0, m - 1
        total_int = sum(len(row) for row in matrix)
        res = []

        while len(res) < total_int:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1

            for j in range(t, b + 1):
                res.append(matrix[j][r])
            r -= 1

            if len(res) < total_int:
                for i in range(r, l - 1, -1):
                    res.append(matrix[b][i])
                b -=1

                for j in range(b, t - 1, -1):
                    res.append(matrix[j][l])
                l += 1
        return res