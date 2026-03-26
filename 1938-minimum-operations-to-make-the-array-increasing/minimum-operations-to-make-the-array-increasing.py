class Solution:
    def minOperations(self, nums: List[int]) -> int:
        operations = 0
        prev = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            
            if num > prev:
                prev = num
            else:
                operations += prev - num + 1
                prev += 1

        return operations