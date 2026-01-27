class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {} # Optimization
        res = []
        builder = []

        def is_palindrome(substring):
            l, r = 0, len(substring) - 1
            while l < r:
                if substring[l] != substring[r]:
                    return False
                l += 1
                r -= 1
            return True

        # We are trying to find palindrome partitioning for s[i:]
        def dfs(i):
            if i == len(s):
                res.append(builder.copy())
                return

            for j in range(i + 1, len(s) + 1):
                if (i, j) not in memo:
                    memo[(i, j)] = is_palindrome(s[i:j])
                if memo[(i, j)]:
                    builder.append(s[i:j])
                    dfs(j)
                    builder.pop()

        dfs(0)
        return res
