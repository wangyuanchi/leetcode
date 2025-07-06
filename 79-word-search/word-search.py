class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def search(row, col, index):
            # Base case
            if index == len(word):
                return True

            # Invalid searches
            # Out of bound
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            # Already visited
            if visited[row][col]:
                return False

            if board[row][col] == word[index]:
                visited[row][col] = True
                for direction in DIRECTIONS:
                    found = search(row + direction[0], col + direction[1], index + 1)
                    if found:
                        return True
                visited[row][col] = False # Backtracking
            
            return False

        for row in range(len(board)):
            for col in range(len(board[row])):
                found = search(row, col, 0)
                if found:
                    return True

        return False
