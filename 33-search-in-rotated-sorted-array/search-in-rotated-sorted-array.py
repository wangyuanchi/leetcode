class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            middle = left + (right - left) // 2 
            if nums[middle] == target:
                return middle
            
            # case 1: smooth continuity on the left half inclusive middle,
            # i.e. mininum in right half exclusive middle
            if nums[middle] > nums[right]:
                # target in continuity
                if target < nums[middle] and target >= nums[left]: 
                    right = middle - 1
                else:
                    left = middle + 1

            # case 2: smooth continuity on the right half inclusive middle,
            # i.e. minimum in left half inclusive middle
            else:
                # target in continuity
                if target > nums[middle] and target <= nums[right]: 
                    left = middle + 1
                else:
                    right = middle - 1
        
        if nums[left] == target:
            return left
        else:
            return -1