class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # At each index, decide whether to add the value to the current subarray
        # or start a new subarray from current index + 1
        cur = 0
        maxSum = -2**31

        for num in nums:
            cur += num
            maxSum = max(maxSum, cur)

            if cur < 0:
                cur = 0
                
        return maxSum