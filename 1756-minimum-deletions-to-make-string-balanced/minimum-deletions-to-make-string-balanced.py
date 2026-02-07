class Solution:
    def minimumDeletions(self, s: str) -> int:
        """
        This is a greedy question.
        min_deletions(i) refers to the min deletions to make s[:i + 1] balanced.
        if s[i] == "b": min_deletions(i) = min_deletions(i - 1)
        if s[i] == "a": min_deletions(i) = min(min_deletions(i - 1) + 1, count of "b" in s[:i + 1])
        """

        deletions = 0
        b_count = 0

        for char in s:
            if char == "b":
                b_count += 1
            else:
                deletions = min(deletions + 1, b_count)

        return deletions
