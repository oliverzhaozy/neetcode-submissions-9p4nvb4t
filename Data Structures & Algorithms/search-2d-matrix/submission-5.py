class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        target_row = 0
        while l <= r:
            m = (l + r) // 2
            first_num, last_num = matrix[m][0], matrix[m][-1]

            if first_num > target:
                r = m - 1
            elif last_num < target:
                l = m + 1
            else:
                target_row = m
                break
            
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            num = matrix[target_row][m]

            if num > target:
                r = m -1
            elif num < target:
                l = m + 1
            else:
                return True
        return False
