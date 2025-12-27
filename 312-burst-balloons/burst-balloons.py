class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        Brute force - Decision Tree: O(n!)
        Brute force - Decision Tree with Memoization:
            e.g. [1,2,3,4]: We pop 1 then 2 vs 2 then 1, both end up with [3, 4]
            We store the state of the remaining array's best outcome: O(n*2^n)
        There are 2^n subproblems, which is too much, suppose we try to cut it to n^2.
        A naive way might be to try to split the array into 2 sub-arrays
        based on the element we choose.
            e.g. [1,2,3,4]: If we choose 3, then the sub-arrays are [1,2] and [4].
            Then, the best outcome looks to be 3*2*4 + best([1,2]) + best([4]).
            However, this sub-array cannot be memoized because it depends
            also on the side values, not just the sub-array itself.
            Consider choosing 4, then 3. At that point, best([1,2]) == 4, but
            best([1,2]) in the previous example == 10.
        It is clear that best(sub-arrays) also depend on the side values.
        The intuition here is now that we want to fix this side values.
        So, instead of asking "What happens if I pop this balloon now?",
        ask "What happens if I pop this balloon last?".
            e.g. Using the same example, If we pop 3 the last, then
            best([1,2,3,4]) == 3 + best([1,2]) + best([4]).
            Notice that if we choose 4, then 3 now. best([1,2]) == 9,
            which is the same as the previous example == 9.
        This is because since we pop 3 the last, we know that the side value is fixed.
        Now, we can use the result from our sub-problem.
        There are n^2 subproblems, each taking O(n) -> Time complexity: O(n^3).
        """
        # Amend nums to make calculations easier
        original_length = len(nums)
        nums.append(1)
        nums.insert(0, 1)

        memo = {} # Key: (l, r)

        # Returns the max coins from bursting balloons within [l, r]
        def dp(l, r):
            # Memo
            if (l, r) in memo:
                return memo[(l, r)]

            # Base case
            if l > r:
                return 0

            # Main logic
            max_coins = 0
            for i in range(l, r + 1):
                # If we burst the balloon at i last
                coins = nums[i] * nums[l - 1] * nums[r + 1]
                coins += dp(l, i - 1) + dp(i + 1, r)
                max_coins = max(max_coins, coins)

            memo[(l, r)] = max_coins
            return max_coins

        return dp(1, original_length)
