class Solution:
    def longestPalindrome(self, s: str) -> str:
        # memo[i][j] => Whether the substring s[i:j+1] is a palindrome
        memo = [[False for _ in range(len(s))] for _ in range(len(s))]
        longest = 1
        l, r = 0, 0

        # The memo table has important values in the top-right triangle
        for i in range(len(s)):
            # Base case 1: Single character
            memo[i][i] = True
            # Base case 2: Double character
            if i + 1 < len(s) and s[i] == s[i + 1]:
                memo[i][i + 1] = True
                if longest == 1:
                    longest = 2
                    l, r = i, i + 1

        # A square in this triangle requires the value in its bottom left
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                if memo[i + 1][j - 1] and s[i] == s[j]:
                    memo[i][j] = True
                    if longest < j - i + 1:
                        longest = j - i + 1
                        l, r = i, j
            
        return s[l:r+1]