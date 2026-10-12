# https://leetcode.com/problems/maximum-gap/solutions/8559733/maximum-gap-in-on-bucket-sort-pigeonhole-d14x/
class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n = len(nums)
        mn, mx = min(nums), max(nums)

        if mn == mx:
            return 0

        bucket_size = (mx - mn + n - 2) // (n - 1)
        bucket_count = 1 + (mx - mn) // bucket_size
        min_bucket = [float("inf")] * bucket_count
        max_bucket = [-float("inf")] * bucket_count

        for num in nums:
            idx = (num - mn) // bucket_size
            min_bucket[idx] = min(min_bucket[idx], num)
            max_bucket[idx] = max(max_bucket[idx], num)

        res = 0
        prev = max_bucket[0]

        for i in range(1, bucket_count):
            if min_bucket[i] == float("inf"):
                continue

            res = max(res, min_bucket[i] - prev)
            prev = max_bucket[i]

        return res
