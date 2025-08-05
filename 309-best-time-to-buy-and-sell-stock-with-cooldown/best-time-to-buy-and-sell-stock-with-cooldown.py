class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        # Returns the maximum profit attainable given prices[i:]
        def dp(i):
            # Base case
            if i >= len(prices) - 1:
                return 0

            # Memo
            if i in memo:
                return memo[i]

            lowest = prices[i]
            maxProfit = 0
            for j in range(i, len(prices)):
                if prices[j] <= lowest:
                    lowest = prices[j]
                else:
                    maxProfit = max(maxProfit, prices[j] - lowest + dp(j + 2))
            
            memo[i] = maxProfit
            return maxProfit

        return dp(0)