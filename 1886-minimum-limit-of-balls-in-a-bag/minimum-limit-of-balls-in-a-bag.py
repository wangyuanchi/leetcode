class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can_split(limit):
            operations = 0
            for num in nums:
                if num > limit:
                    operations += num // limit
                    if num % limit == 0:
                        operations -= 1
            return operations <= maxOperations

        l, r = 1, max(nums)

        while l < r:
            m = l + (r - l) // 2
            if can_split(m):
                r = m
            else:
                l = m + 1

        return l
