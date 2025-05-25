import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 3-way in place partition between left and right using pivot index
        # returns the inclusive index range of the duplicates
        def partition(l, r, p):
            # swap pivot value to the end
            nums[p], nums[r] = nums[r], nums[p]

            # [l, a1) is less than pivot
            # [a1, a2) is equal to pivot
            # [a2, r) is more than pivot
            a1, a2 = l, l

            for i in range(l, r):
                if nums[i] == nums[r]:
                    nums[i], nums[a2] = nums[a2], nums[i]
                    a2 += 1
                elif nums[i] < nums[r]:
                    nums[i], nums[a2] = nums[a2], nums[i]
                    nums[a2], nums[a1] = nums[a1], nums[a2]
                    a2 += 1
                    a1 += 1

            # swap pivot back into the correct position
            nums[a2], nums[r] = nums[r], nums[a2]
            a2 += 1

            return (a1, a2 - 1)

        # quick select between left and right for target index
        def select(l, r, target):
            # base case
            if l == r: 
                return nums[target]

            p = random.randint(l, r)
            index_range = partition(l, r, p)
            p1, p2 = index_range[0], index_range[1]

            if target >= p1 and target <= p2: 
                return nums[target]
            elif target < p1: 
                return select(l, p1 - 1, target)
            else: 
                return select(p2 + 1, r, target)

        idx_in_sorted = len(nums) - k
        return select(0, len(nums) - 1, idx_in_sorted)