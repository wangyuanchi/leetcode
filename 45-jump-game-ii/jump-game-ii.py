class Solution:
    def jump(self, nums: List[int]) -> int:
        # We want the min number of jumps for the last index
        # Can get the min number of jumps for all indexes
        # Maintain 2 points and shift both to contain all indexes for the curStep
        l, r = 0, 1 # [l, r)
        curStep = 0
        targetIndex = len(nums) - 1

        # While target index is not in the window
        # Note there will always be an answer
        while not (targetIndex >= l and targetIndex < r):
            newR = 0
            for i in range(l, r):
                newR = max(newR, i + nums[i])
            l = r
            r = newR + 1
            curStep += 1

        return curStep