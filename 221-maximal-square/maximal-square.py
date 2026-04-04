class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = {}
        max_length = 0

        def dp(r, c):
            if r < 0 or c < 0:
                return 0
            
            if matrix[r][c] == "0":
                return 0

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = min(
                dp(r - 1, c),
                dp(r - 1, c - 1),
                dp(r, c - 1)
            ) + 1

            nonlocal max_length

            max_length = max(max_length, memo[(r, c)])

            return memo[(r, c)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dp(r, c)

        return max_length ** 2