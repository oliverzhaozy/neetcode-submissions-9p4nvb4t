class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        curPath = [["."] * n for _ in range(n)]
        res = []
        col, pos_diag, neg_diag = set(), set(), set()

        def backtrack(r, curPath):
            # Base case
            if r == n:
                res.append(["".join(row) for row in curPath])
                return

            for c in range(n):
                if c in col or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                curPath[r][c] = "Q"

                backtrack(r + 1, curPath)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                curPath[r][c] = "."

        backtrack(0, curPath)
        return res