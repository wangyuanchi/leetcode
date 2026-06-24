class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        row_state = defaultdict(set)
        col_state = defaultdict(set)
        square_state = defaultdict(set)

        def update_state_add(row, col, val):
            row_state[row].add(val)
            col_state[col].add(val)
            square_state[(row // 3, col // 3)].add(val)

        def update_state_remove(row, col, val):
            row_state[row].remove(val)
            col_state[col].remove(val)
            square_state[(row // 3, col // 3)].remove(val)

        def is_valid(row, col, val):
            return (
                val not in row_state[row] and
                val not in col_state[col] and 
                val not in square_state[(row // 3, col // 3)]
            )

        def get_next_cell(r, c):
            if c != 8:
                return (r, c + 1)
            else:
                return (r + 1, 0)

        def backtrack(r, c): # return whether we have completed or not
            if r == 9:
                return True

            next_r, next_c = get_next_cell(r, c)

            if board[r][c] != ".":
                return backtrack(next_r, next_c)

            for val in range(1, 10):
                val = str(val)
                if not is_valid(r, c, val):
                    continue

                board[r][c] = val
                update_state_add(r, c, val)
                if backtrack(next_r, next_c):
                    return True

                update_state_remove(r, c, val)
                board[r][c] = "."

            return False

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    update_state_add(row, col, board[row][col])

        backtrack(0, 0)
