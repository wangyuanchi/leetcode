class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def dfs(row, col):
            # Base case 1: Out of bound
            if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1:
                return
            # Base case 2: X
            if board[row][col] == "X":
                return
            # Base case 3: Visited already
            if visited[row][col]:
                return

            visited[row][col] = True

            for direction in DIRECTIONS:
                dfs(row + direction[0], col + direction[1])

        for row in range(len(board)):
            for col in range(len(board[0])):
                if row == 0 or row == len(board) - 1:
                    dfs(row, col)
                    continue
                if col == 0 or col == len(board[0]) - 1:
                    dfs(row, col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if not visited[row][col]:
                    board[row][col] = "X"                