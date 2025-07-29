class Solution:
    def rob(self, nums: List[int]) -> int:
        # Don't rob index 0
        memo = {}
        numsCopy = nums[1:]

        # Rob houses from i onwards for numsCopy
        # Returns the max amount of money able to be robbed
        def dp(i):
            if i >= len(numsCopy):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(numsCopy[i] + dp(i + 2), dp(i + 1))
            return memo[i]

        # Don't rob index 0
        v1 = dp(0)

        # Rob index 0
        memo = {}
        numsCopy = nums[2:len(nums) - 1]
        v2 = nums[0] + dp(0)

        return max(v1, v2)