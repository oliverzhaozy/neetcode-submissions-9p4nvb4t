class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save topLeft as temp variable
                topLeft = matrix[top][l + i]

                # assign bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # assign bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # assign top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # assign top left to top right
                matrix[top + i][r] = topLeft
            l += 1
            r -= 1