class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        target_window = total - x
        cur_window = 0
        l = 0
        num_windows = -1

        for r in range(len(nums)):
            cur_window += nums[r]

            while l <= r and cur_window > target_window:
                cur_window -= nums[l]
                l += 1
            
            if cur_window == target_window:
                num_windows = max(num_windows, r - l + 1)

        return -1 if num_windows == -1 else len(nums) - num_windows
