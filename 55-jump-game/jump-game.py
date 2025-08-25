class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curFurthest, curIndex = 0, 0
        while curIndex != len(nums) and curIndex <= curFurthest:
            curFurthest = max(curFurthest, nums[curIndex] + curIndex)
            curIndex += 1
        return curFurthest >= len(nums) - 1