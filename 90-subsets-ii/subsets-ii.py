class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = [] # Builder

        nums = sorted(nums)

        # Whether the value at index i will be in the subset or not
        def dfs(i):
            # Base case
            if i == len(nums):
                res.append(subset.copy())
                return

            # The value is in the subset
            subset.append(nums[i])
            dfs(i + 1)

            # The value is not in the subset (skip duplicates)
            subset.pop()
            for j in range(i + 1, len(nums) + 1):
                # Base case
                if j == len(nums):
                    dfs(j)
                    break
                    
                if (nums[j] == nums[j - 1]):
                    continue
                else:
                    dfs(j)
                    break


        dfs(0)
        return res
