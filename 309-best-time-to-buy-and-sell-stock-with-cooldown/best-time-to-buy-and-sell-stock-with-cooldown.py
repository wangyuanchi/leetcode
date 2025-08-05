class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Draw out the decision tree
        # At each node, either we do a cooldown, or we buy/sell
        # Remember that if we sell, we cannot buy the day after

        # The key (day, buying) represents that I am at the state of being on that day,
        # having the choice to buy or don't buy or sell or don't sell
        memo = {}

        # Returns the max profit attainable given the state of the key
        def dp(day, buying):
            # Base case
            if day >= len(prices):
                return 0

            # Memo
            if (day, buying) in memo:
                return memo[(day, buying)]

            cooldown = dp(day + 1, buying) # Don't buy/sell
            if buying:
                memo[(day, buying)] = max(cooldown, - prices[day] + dp(day + 1, not buying))
            else:
                memo[(day, buying)] = max(cooldown, prices[day] + dp(day + 2, not buying))

            return memo[(day, buying)]

        return dp(0, True)