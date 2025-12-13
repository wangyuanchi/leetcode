class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, pd, nd = set(), set(), set()
        board = [["." for _ in range(n)] for _ in range(n)] # Top-left is (0, 0)
        res = []

        def dfs(r):
            # Base case
            if r == n:
                res.append(["".join(board[r]) for r in range(n)])
                return

            # Add the queen
            for c in range(n):
                pd_index = r + c
                nd_index = r - c
                if c not in col and pd_index not in pd and nd_index not in nd:
                    board[r][c] = "Q"
                    col.add(c)
                    pd.add(pd_index)
                    nd.add(nd_index)
                    dfs(r + 1)

                    # Remove the queen
                    board[r][c] = "."
                    col.remove(c)
                    pd.remove(pd_index)
                    nd.remove(nd_index)

        dfs(0)
        return res
