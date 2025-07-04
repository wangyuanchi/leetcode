class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutations = [] # Builder
        
        # All values from index left onwards (inclusive) can be chosen next
        def dfs(left):
            # Base case
            if left == len(nums):
                res.append(permutations.copy())
                return

            for i in range(left, len(nums)):
                # Choosing the value
                permutations.append(nums[i])
                nums[i], nums[left] = nums[left], nums[i]
                dfs(left + 1)

                # Backtracking
                permutations.pop()
                nums[i], nums[left] = nums[left], nums[i]

        dfs(0)
        return res