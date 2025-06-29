class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # all subsets
        subset = [] # subset builder

        # dfs(i) means "Do I add the number at index i"
        def dfs(i):
            if (i == len(nums)):
                res.append(subset.copy())
                return

            # Include the current value
            subset.append(nums[i])
            dfs(i + 1)

            # Don't include the current value
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res