class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        # Returns the number of unique paths to 
        # grid[m - 1][n - 1] from the current coord
        def dp(x, y):
            # Base case 1: Out of bound
            if x >= m or y >= n:
                return 0
            # Base case 2: Right before trophy or on trophy
            if x == m - 2 and y == n - 1:
                return 1
            if x == m - 1 and y == n - 2:
                return 1
            if x == m - 1 and y == n - 1:
                return 1
            
            # Memo
            if memo[x][y] != -1:
                return memo[x][y]
            
            memo[x][y] = dp(x + 1, y) + dp(x, y + 1)
            return memo[x][y]

        return dp(0, 0)