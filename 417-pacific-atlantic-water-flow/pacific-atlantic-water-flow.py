class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        PACIFIC, ATLANTIC = 0, 1
        # [False, False] is for visited for [Pacific, Atlantic]
        visited = [[[False, False] for j in range(len(heights[0]))] for i in range(len(heights))]
        q = deque()

        for row in range(len(heights)):
            for col in range(len(heights[row])):
                # Add nodes for Atlantic
                if row != len(heights) - 1:
                    if col == len(heights[row]) - 1:
                        visited[row][col][ATLANTIC] = True
                        q.append((row, col, ATLANTIC))
                else:
                    visited[row][col][ATLANTIC] = True
                    q.append((row, col, ATLANTIC))
                # Add nodes for Pacific
                if row == 0:
                    visited[row][col][PACIFIC] = True
                    q.append((row, col, PACIFIC))
                else:
                    if col == 0:
                        visited[row][col][PACIFIC] = True
                        q.append((row, col, PACIFIC))
        
        while len(q) > 0:
            coord = q.popleft()
            r, c, ocean = coord[0], coord[1], coord[2]
            
            for direction in DIRECTIONS:
                new_r = r + direction[0]
                new_c = c + direction[1]

                # Check out of map
                if new_r < 0 or new_c < 0 or new_r > len(heights) - 1 or new_c > len(heights[0]) - 1:
                    continue
                # If the coordinate cannot be reached from the new coordinate
                if heights[new_r][new_c] < heights[r][c]:
                    continue

                # Check visited
                if not visited[new_r][new_c][ocean]:
                    visited[new_r][new_c][ocean] = True
                    q.append((new_r, new_c, ocean))

        res = []
        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if visited[row][col][PACIFIC] and visited[row][col][ATLANTIC]:
                    res.append([row, col])

        return res