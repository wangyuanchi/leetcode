class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text2))] for _ in range(len(text1))]

        # Fill in base cases
        flag = True
        for i in range(len(text1)):
            if flag:
                if text2[0] == text1[i]:
                    memo[i][0] = 1
                    flag = False
            else:
                memo[i][0] = 1

        flag = True
        for i in range(len(text2)):
            if flag:
                if text1[0] == text2[i]:
                    memo[0][i] = 1
                    flag = False
            else:
                memo[0][i] = 1

        # Fill in dp cases
        # If the substring has the same ending character,
        # LCS = LCS of both substring without the ending character + 1
        # Otherwise, LCS = max of both cases where 1 substring loses 1 character
        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                if text1[i] == text2[j]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])

        return memo[len(text1) - 1][len(text2) - 1]