class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {} # Key: (s_index, t_index)

        # Returns the number of distinct subsequences
        # of s[s_index:] that are equal to t[t_index:]
        def dp(s_index, t_index):
            # Memo
            if (s_index, t_index) in memo:
                return memo[(s_index, t_index)]

            # Base case
            if t_index == len(t):
                return 1
            if s_index == len(s):
                return 0

            # Main logic
            if s[s_index] != t[t_index]:
                res = dp(s_index + 1, t_index)
            else:
                res = dp(s_index + 1, t_index + 1) + dp(s_index + 1, t_index)

            memo[(s_index, t_index)] = res
            return res

        return dp(0, 0)
