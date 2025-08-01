class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        # Returns the fewest number of coins to make up amt
        def dp(amt):
            if amt < 0:
                return -1

            if amt == 0:
                return 0

            if amt in memo:
                return memo[amt]

            val = 2**31 - 1
            hasValidCombination = False
            for coin in coins:
                if dp(amt - coin) != -1:
                    val = min(val, 1 + dp(amt - coin))
                    hasValidCombination = True

            if hasValidCombination:
                memo[amt] = val
            else:
                memo[amt] = -1

            return memo[amt]

        return dp(amount)