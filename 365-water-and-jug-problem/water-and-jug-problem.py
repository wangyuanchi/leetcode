class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()

        def dfs(a, b):
            if (a, b) in visited:
                return False

            if a + b == target:
                return True

            visited.add((a, b))

            if dfs(x, b): return True
            if dfs(a, y): return True
            if dfs(0, b): return True
            if dfs(a, 0): return True

            # Pour from x to y
            amount_poured = min(y - b, a)
            if dfs(a - amount_poured, b + amount_poured): return True

            # Pour from y to x
            amount_poured = min(x - a, b)
            if dfs(a + amount_poured, b - amount_poured): return True

            return False

        return dfs(0, 0)