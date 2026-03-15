class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def dp(i, have_stock):
            if i == len(prices):
                return 0

            if (i, have_stock) in memo:
                return memo[(i, have_stock)]

            if have_stock:
                memo[(i, have_stock)] = max(dp(i + 1, True), prices[i] + dp(i + 1, False))
            else:
                memo[(i, have_stock)] = max(-prices[i] + dp(i + 1, True), dp(i + 1, False))

            return memo[(i, have_stock)]

        return dp(0, False)