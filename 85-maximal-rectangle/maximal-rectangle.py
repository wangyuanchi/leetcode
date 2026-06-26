class Solution:
    # From LeetCode 84
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights) + 1):
            if i == len(heights):
                height = 0
            else:
                height = heights[i]

            popLeftLimit = i

            while len(stack) > 0 and stack[-1][0] > height:
                popHeight, popLeftLimit = stack.pop()
                maxArea = max(maxArea, popHeight * (i - popLeftLimit))

            stack.append((height, popLeftLimit))

        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        If all the 1s were connected, then the problem easily reduces to LC84
        However, if some 1s were separated, we should go to the base row where
        those 1s are now all connected.
        Hence, the solution is to LC84 all rows, while incrementing the 1 count
        for each column if the cell above is also a 1.
        """
        heights = [int(val) for val in matrix[0]]
        maximal_rectangle = self.largestRectangleArea(heights)

        for row in range(1, len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "0":
                    heights[col] = 0
                else:
                    heights[col] += 1
            maximal_rectangle = max(maximal_rectangle, self.largestRectangleArea(heights))

        return maximal_rectangle
