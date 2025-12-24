class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {} # Key: (row, col)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Returns the longest increasing path starting at this coordinate
        def dp(row, col):
            # Already Memo
            if (row, col) in memo:
                return memo[(row, col)]
                
            # Find valid neighbour coordinates
            valid_neighbours = []
            for r, c in DIRECTIONS:
                new_row, new_col = row + r, col + c
                if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
                    continue
                valid_neighbours.append((new_row, new_col))

            longest = 1 # Base case
            for nb_r, nb_c in valid_neighbours:
                if matrix[nb_r][nb_c] > matrix[row][col]:
                    longest = max(longest, 1 + dp(nb_r, nb_c)) # Main logic

            memo[(row, col)] = longest
            return longest

        longest = 1
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                longest = max(longest, dp(row, col))
        return longest