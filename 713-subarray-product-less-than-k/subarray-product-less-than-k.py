class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        windowProduct = 1
        total = 0

        while r < len(nums):
            windowProduct *= nums[r]

            while l <= r and windowProduct >= k:
                windowProduct /= nums[l]
                l += 1

            total += r - l + 1
            r += 1
        
        return total