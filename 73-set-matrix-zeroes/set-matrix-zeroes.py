class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Use the first row and first column as boolean arrays to indicate
        # whether there is a zero in that row/column (excluding self)
        # Assuming r1 and c1 has no zeros originally, then it is simple
        # Otherwise, we need to find out if there are, then use O(1) space to
        # keep track of whether r1 and c1 should be all zeros in the end.

        r1_all_zero, c1_all_zero = False, False

        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                r1_all_zero = True

        for r in range(len(matrix)):
            if matrix[r][0] == 0:
                c1_all_zero = True

        # Filling in the "boolean array"
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0, 0

        # Filling up the entire matrix
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(1, len(matrix)):
                    matrix[r][c] = 0

        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                for c in range(1, len(matrix[0])):
                    matrix[r][c] = 0

        # Deal with r1 and c1
        if r1_all_zero:
            for c in range(len(matrix[0])):
                matrix[0][c] = 0
        
        if c1_all_zero:
            for r in range(len(matrix)):
                matrix[r][0] = 0
