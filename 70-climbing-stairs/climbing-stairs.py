class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dp(n):
            # Base case
            if n == 1 or n == 2:
                return n
            
            # Memoization
            if n in memo:
                return memo[n]
            
            memo[n] = dp(n - 1) + dp(n - 2)
            return memo[n]

        return dp(n)