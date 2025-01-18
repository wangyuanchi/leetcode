class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        processedLocks = set()

        # stop at the 3rd last number for the lock
        for lock in range(len(nums) - 2): 
            # check duplicates for locks
            if nums[lock] in processedLocks:
                continue
            else:    
                processedLocks.add(nums[lock])

            left, right = lock + 1, len(nums) - 1
            while left < right:
                totalSum = nums[lock] + nums[left] + nums[right]
                if totalSum == 0:
                    result.append([nums[lock], nums[left], nums[right]])
                    
                    # make some change happen by shifting left
                    # left < right to prevent out of bounds
                    currLeft = nums[left]
                    while left < right and currLeft == nums[left]:
                        left += 1 
                elif totalSum > 0:
                    currRight = nums[right]
                    while left < right and currRight == nums[right]:
                        right -= 1
                else:
                    currLeft = nums[left]
                    while left < right and currLeft == nums[left]:
                        left += 1 

        return result