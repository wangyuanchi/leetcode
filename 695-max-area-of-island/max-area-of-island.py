class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))] # For islands only
        DIRECTIONS = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        maxArea = 0

        def findArea(row, col):
            # Base case 1: Out of bounds
            if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
                return 0

            # Base case 2: Water
            if grid[row][col] == 0:
                return 0

            # If visited before, ignore, the area would have already been added
            if visited[row][col]:
                return 0

            area = 1
            visited[row][col] = True

            # Not visited yet
            for direction in DIRECTIONS:
                area += findArea(row + direction[0], col + direction[1])

            return area

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and not visited[row][col]:
                    maxArea = max(maxArea, findArea(row, col))

        return maxArea