class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))] # For islands only
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        islands = 0

        # Visit the whole island
        def visit(row, col):
            # Base case 1: Exceed the map
            if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1:
                return 

            # Base case 2: Water
            if grid[row][col] == "0":
                return
            
            # Now, I must be on island in the map
            if visited[row][col]:
                return

            # Now, I have not visited this square
            visited[row][col] = True
            for direction in DIRECTIONS:
                visit(row + direction[0], col + direction[1])

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands += 1
                    visit(row, col)

        return islands