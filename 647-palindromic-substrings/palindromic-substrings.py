class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2D memo table where memo[i][j] represents whether the
        # substring s[i][j+1] is a palindrome
        memo = [[False for _ in range(len(s))] for _ in range(len(s))]
        count = 0

        # Base cases
        for i in range(len(s)):
            memo[i][i] = True
            count += 1
            if i != len(s) - 1 and s[i] == s[i + 1]:
                memo[i][i + 1] = True
                count += 1

        # Loop all substrings
        # From bottom of upper-right triangle
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                if memo[i + 1][j - 1] and s[i] == s[j]:
                    memo[i][j] = True
                    count += 1

        return count