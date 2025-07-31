class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        # Returns the number of ways to decode the substring s[i:]
        def dp(i):
            # Base cases
            if i == len(s): # Hit when dp(i + 2), e.g. s == "12"
                return 1
            if s[i] == "0":
                return 0
            if i == len(s) - 1:
                return 1
        
            # Memo
            if i in memo:
                return memo[i]

            # At least 2 digits from here on, and does not start with "0"
            if s[i] == "1":
                memo[i] = dp(i + 1) + dp(i + 2)
            elif s[i] == "2" and s[i + 1] in "0123456":
                memo[i] = dp(i + 1) + dp(i + 2)
            else:
                memo[i] = dp(i + 1)

            return memo[i]

        return dp(0)