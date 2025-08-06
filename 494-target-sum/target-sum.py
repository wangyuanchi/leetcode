class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        # Returns the number of ways to get subtarget t only using
        # values from nums[i:]
        def dp(i, t):
            # Base case
            if i == len(nums):
                if t == 0:
                    return 1
                else:
                    return 0

            # Memo
            if (i, t) in memo:
                return memo[(i, t)]

            memo[(i, t)] = dp(i + 1, t - nums[i]) + dp(i + 1, t + nums[i])
            return memo[(i, t)]

        return dp(0, target)