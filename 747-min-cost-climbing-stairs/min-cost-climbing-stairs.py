class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(currentIndex):
            # Base cases
            if currentIndex == len(cost):
                return 0
            if currentIndex == len(cost) - 1 or currentIndex == len(cost) - 2:
                return cost[currentIndex]

            # Memo
            if currentIndex in memo:
                return memo[currentIndex]

            memo[currentIndex] = cost[currentIndex] + min(dp(currentIndex + 1), dp(currentIndex + 2))
            return memo[currentIndex]
        
        return min(dp(0), dp(1))