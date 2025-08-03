class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        # The length of the LIS at index i
        def dp(i):
            # Base case
            if i == len(nums) - 1:
                return 1

            # Memo
            if i in memo:
                return memo[i]

            curMax = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    curMax = max(curMax, 1 + dp(j))
            
            memo[i] = curMax
            return curMax

        LIS = 1
        for i in range(len(nums)):
            LIS = max(LIS, dp(i))

        return LIS