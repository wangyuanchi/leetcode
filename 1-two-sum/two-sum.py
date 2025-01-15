class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = {} # key is num, value is index
        for i in range(len(nums)):
            required = target - nums[i]
            if required in indexDict:
                return [indexDict[required], i]
            else:
                indexDict[nums[i]] = i