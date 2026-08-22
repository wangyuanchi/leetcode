class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Prefix[i] returns sum of values from nums[0] to nums[i] inclusive
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i - 1])

        count = 0
        freq = {}
        freq[0] = 1
        
        for i in range(len(prefix)):
            window_sum_from_zero = prefix[i]
            target = window_sum_from_zero - goal

            if target in freq:
                count += freq[target]

            if window_sum_from_zero not in freq:
                freq[window_sum_from_zero] = 0
            freq[window_sum_from_zero] += 1

        return count