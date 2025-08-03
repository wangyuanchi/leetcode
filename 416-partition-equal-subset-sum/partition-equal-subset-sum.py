class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Subproblem definition:
        # Find all possible sums for a subarray of nums starting at i
        dp = set()
        target = sum(nums)

        # Impossible if total sum is odd
        if target % 2 == 1:
            return False
        target = target / 2
        
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            val = nums[i]
            dpNext = set()
            for s in dp:
                # Early return
                if val + s == target:
                    return True

                dpNext.add(s)
                dpNext.add(val + s)

            dp = dpNext

        return target in dp