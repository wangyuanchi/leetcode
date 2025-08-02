class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Subproblem definition:
        # Given the largest & smallest product of any subarray ending at index i,
        # find the largest & smallest product of any subarray ending at index i + 1
        # Then, return the max of the largest products for all indexes

        latestMax, latestMin = 1, 1
        globalMax = nums[0]

        for num in nums:
            tempMax = latestMax

            # This covers all cases
            # ++, +-, -- for latestMax and latestMin, + 0 - for num
            latestMax = max(num, num * latestMax, num * latestMin)
            latestMin = min(num, num * tempMax, num * latestMin)
            
            globalMax = max(globalMax, latestMax)   

        return globalMax