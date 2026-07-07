class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        thieves = deque()
        visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    thieves.append((row, col, 0))
                    visited.add((row, col))

        safety_matrix = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        while len(thieves) > 0:
            row, col, safeness = thieves.popleft()
            safety_matrix[row][col] = safeness

            for d1, d2 in directions:
                new_row, new_col = row + d1, col + d2

                if new_row < 0 or new_col < 0 or new_row >= len(grid) or new_col >= len(grid[0]):
                    continue
                
                if (new_row, new_col) in visited:
                    continue

                visited.add((new_row, new_col))
                thieves.append((new_row, new_col, safeness + 1))
                
        max_heap = [(safety_matrix[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        
        while len(max_heap) > 0:
            current_safety, row, col = heapq.heappop_max(max_heap)
            
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return current_safety

            for d1, d2 in directions:
                new_row, new_col = row + d1, col + d2

                if new_row < 0 or new_col < 0 or new_row >= len(grid) or new_col >= len(grid[0]):
                    continue
                
                if (new_row, new_col) in visited:
                    continue

                visited.add((new_row, new_col))

                new_safety = safety_matrix[new_row][new_col]

                heapq.heappush_max(max_heap, (min(new_safety, current_safety), new_row, new_col))
