class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # 1. It is optimal to use all rocks.
        # - Suppose we do not, then using the missed rock can worse case change nothing,
        # - but best case decrease the cost.
        # 2. Losely: It is not optimal to use any 2 adjacent rocks in 1 jump
        # - Loose proof: If I do so, e.g. a, b, c, d and b to c, then eventually I will
        # - need to do d to a, and a lower max length would be from b to d then c to a.
        # 1 and 2 results in the optimal being doing alternate jumps, odd and even indexes.
        # By considering how the jumps look like for small cases, e.g. 4 or 5
        # The answer is max(A[i] - A[i - 2] for all valid i)
        if len(stones) == 2:
            return stones[1]

        res = 0
        for i in range(2, len(stones)):
            res = max(res, stones[i] - stones[i - 2])
        return res