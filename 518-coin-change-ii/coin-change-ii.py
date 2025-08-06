class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Subproblem definition:
        # Total combinations to make up a certain amt
        # only using coins from index i onwards
        memo = {}

        def dp(amt, i):
            # Base case 1: Out of Bound
            if i >= len(coins) or amt < 0:
                return 0
            
            # Base case 2: Found a combination
            if amt == 0:
                return 1

            # Memo
            if (amt, i) in memo:
                return memo[(amt, i)]
            
            memo[(amt, i)] = dp(amt, i + 1) + dp(amt - coins[i], i)
            return memo[(amt, i)]

        return dp(amount, 0)