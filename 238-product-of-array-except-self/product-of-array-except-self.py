class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProducts = [1]*len(nums)
        rightProducts = [1]*len(nums)

        for i in range(1, len(nums)):
            leftProducts[i] = leftProducts[i-1] * nums[i-1]

        # Reverse order
        for i in range(len(nums) -1 -1, -1, -1):
            rightProducts[i] = rightProducts[i+1] * nums[i+1]

        result = []
        for i in range(len(nums)):
            result.append(leftProducts[i] * rightProducts[i])

        return result