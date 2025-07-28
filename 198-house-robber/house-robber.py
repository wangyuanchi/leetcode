class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        # Either rob the hose at index or don't rob
        # Returns the max amount of money I can rob from i inclusive
        def dp(i):
            # Base case
            if i >= len(nums):
                return 0
            
            # Memo
            if i in memo:
                return memo[i]

            memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return memo[i]

        return dp(0)