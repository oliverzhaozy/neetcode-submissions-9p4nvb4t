class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) 
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        mid_row = 0

        while top <= bottom:
            mid_row = (top + bottom) // 2
            curr = matrix[mid_row][-1]

            if curr > target:
                if matrix[mid_row][0] <= target:
                    break
                bottom = mid_row - 1
            elif curr < target:
                top = mid_row + 1
            else:
                return True
        
        while left <= right:
            mid_col = (left + right) // 2
            curr = matrix[mid_row][mid_col]
            
            if curr > target:
                right = mid_col - 1
            elif curr < target:
                left = mid_col + 1
            else:
                return True
        
        return False