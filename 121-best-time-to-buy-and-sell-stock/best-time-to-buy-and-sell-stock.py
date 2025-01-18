class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price <= lowestPrice:
                lowestPrice = price
            else:
                maxProfit = max(maxProfit, price - lowestPrice)
        
        return maxProfit