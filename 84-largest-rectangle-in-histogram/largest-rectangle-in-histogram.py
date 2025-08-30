class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # At least 1 height is completely in the largest rectangle (Proof by contradiction)
        # Check for all heights using a monotonically increasing stack
        stack = [] # Element: (height, index, leftLimit)
        maxArea = 0

        for i in range(len(heights) + 1):
            # Additional run to clear remaining elements potentially left in the stack
            if i == len(heights):
                height = 0
            else:
                height = heights[i]

            popLeftLimit = i

            while len(stack) > 0 and stack[-1][0] > height:
                popHeight, popIndex, popLeftLimit = stack.pop()
                maxArea = max(maxArea, popHeight * (i - popLeftLimit))

            stack.append((height, i, popLeftLimit))

        return maxArea