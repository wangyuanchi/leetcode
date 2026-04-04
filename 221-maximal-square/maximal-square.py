class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        memo = [0] * len(matrix[0])
        max_length = 0

        for r in range(len(matrix)):
            diag, left = 0, 0
            for c in range(len(matrix[0])):
                val = matrix[r][c]

                cur_length = 1 + min(
                    diag, left, memo[c]
                ) if val == "1" else 0

                # update memo and pointers
                diag = memo[c]
                memo[c] = cur_length
                left = cur_length

                max_length = max(max_length, cur_length)
        
        return max_length ** 2
