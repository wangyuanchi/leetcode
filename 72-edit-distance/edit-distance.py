class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {} # Key is (i, j) and value is the min no. of operations to go from word1[i:] to word2[j:]

        def dp(i, j):
            # Base case
            if i == len(word1) and j == len(word2):
                return 0

            if i == len(word1):
                return len(word2[j:])

            if j == len(word2):
                return len(word1[i:])

            # Memo
            if (i, j) in memo:
                return memo[(i, j)]

            # Main logic
            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i+1, j+1)
            else:
                # Insert, delete and replace in this order
                memo[(i, j)] = 1 + min(dp(i, j+1), dp(i+1, j), dp(i+1, j+1))
            return memo[(i, j)]

        return dp(0, 0)