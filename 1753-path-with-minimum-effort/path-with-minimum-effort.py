class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        min_heap = [(0, 0, 0)] # first value is the mad, next two are the coordinates
        visited = set()

        while len(min_heap) > 0:
            cur_mad, row, col = heapq.heappop(min_heap)

            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return cur_mad

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for d1, d2 in directions:
                new_row, new_col = row + d1, col + d2

                if new_row < 0 or new_col < 0 or new_row >= len(heights) or new_col >= len(heights[0]):
                    continue
    
                new_mad = max(cur_mad, abs(heights[row][col] - heights[new_row][new_col]))

                heapq.heappush(min_heap, (new_mad, new_row, new_col))
