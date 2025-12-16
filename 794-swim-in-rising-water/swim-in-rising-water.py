class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        source = (grid[0][0], 0, 0)
        pq = [source]
        heapq.heapify(pq)
        visited = set()
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_max = source[0]

        while len(pq) > 0:
            value, r, c = heapq.heappop(pq)

            visited.add(value)
            cur_max = max(cur_max, value) # Result is the max of all popped values
            
            if value == grid[-1][-1]:
                return cur_max

            for d1, d2 in DIRECTIONS:
                new_r, new_c = r + d1, c + d2
                if new_r < 0 or new_c < 0 or new_r >= len(grid) or new_c >= len(grid[0]):
                    continue

                if grid[new_r][new_c] in visited:
                    continue

                heapq.heappush(pq, (grid[new_r][new_c], new_r, new_c))