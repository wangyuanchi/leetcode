class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l_row, r_row = x, x + k - 1

        while l_row < r_row:
            for i in range(y, y + k):
                grid[l_row][i], grid[r_row][i] = grid[r_row][i], grid[l_row][i]
            l_row += 1
            r_row -= 1

        return grid