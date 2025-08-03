class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        # Returns whether the substring s[i:] can be broken properly
        def dp(i):
            # Base case
            if s[i:] in wordSet:
                return True

            # Memo
            if i in memo:
                return memo[i]

            memo[i] = False
            for j in range(i + 1, len(s)):
                if dp(j) and s[i:j] in wordSet:
                    memo[i] = True
                    break

            return memo[i]
        
        return dp(0)