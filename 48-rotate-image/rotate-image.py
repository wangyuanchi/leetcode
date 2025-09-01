class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # (row, col) => (col, n - 1 - row)
        # Because we need to do it in place, we do it for 4 cells per ring
        for i in range(n // 2): # Total number of rings
            for j in range(i, n - i - 1): # Number of 4 cell swaps per ring
                # Swap 1
                matrix[i][j], matrix[j][n - 1 - i] = matrix[j][n - 1 - i], matrix[i][j]

                # Swap 2
                matrix[i][j], matrix[n - 1 - i][n - 1 - j] = \
                        matrix[n - 1 - i][n - 1 - j], matrix[i][j]

                # Swap 3
                matrix[i][j], matrix[n - 1 - j][n - 1 - (n - 1 - i)] = \
                        matrix[n - 1 - j][n - 1 - (n - 1 - i)], matrix[i][j]