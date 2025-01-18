class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxAmount = 0

        while left < right:
            maxAmount = max(maxAmount, (right - left)*min(height[left], height[right]))
            
            # if the limiting is the left or they are equal
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maxAmount  