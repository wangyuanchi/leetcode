class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        successor = len(nums)

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] > target:
                successor = m
                r = m - 1
            else:
                l = m + 1
        
        return successor
