class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        Example of repeated work:
        s = "aaaa"
        p = "a*a*a*a*"
        dp(0, 0) -> dp(0, 2) or dp(1, 0)
        dp(0, 2) -> dp(0, 4) or dp(1, 2) [repeated]
        dp(1, 0) -> dp(1, 2) [repeated] or dp(2, 0)
        """
        memo = {} # Key: (i, j)
        
        # Returns if s[i:] matches p[j:]
        def dp(i, j):
            # Memoization
            if (i, j) in memo:
                return memo[(i, j)]

            # Base cases
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False
            if i == len(s):
                # Remaning part should be something like "a*.*" to be True
                if (len(p) - j) % 2 != 0:
                    return False
                res = True
                for k in range(j + 1, len(p), 2):
                    if p[k] != "*":
                        res = False
                        break
                memo[(i, j)] = res
                return res
            
            # Main logic
            res = False
            if j + 1 < len(p) and p[j + 1] == "*":
                if p[j] == "." or p[j] == s[i]:
                    res = dp(i, j + 2) or dp(i + 1, j)
                else:
                    res = dp(i, j + 2)
            else:
                if p[j] == "." or p[j] == s[i]:
                    res = dp(i + 1, j + 1)
                else:
                    res = False

            memo[(i, j)] = res
            return res

        return dp(0, 0)