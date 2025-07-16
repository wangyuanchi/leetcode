class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottenTime = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]
        DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1) ]
        q = deque() # BFS

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rottenTime[row][col] = 0
                    q.append((row, col))

        while len(q) > 0:
            coord = q.popleft()
            for direction in DIRECTIONS:
                row = coord[0] + direction[0]
                col = coord[1] + direction[1]

                # Check if out of bounds
                if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
                    continue
                if grid[row][col] == 0:
                    continue
                if rottenTime[row][col] != -1: # Visited already
                    continue
                
                rottenTime[row][col] = rottenTime[coord[0]][coord[1]] + 1
                q.append((row, col))

        minMinutes = -1
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    continue
                if rottenTime[row][col] == -1:
                    return -1
                minMinutes = max(minMinutes, rottenTime[row][col])
        
        if minMinutes == -1:
            return 0
        else:
            return minMinutes
        