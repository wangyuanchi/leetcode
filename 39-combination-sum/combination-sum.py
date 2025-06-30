class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = [] # Builder

        def dfs(i, sum):
            # Before we make the decision at the current node, check the base cases
            if sum == target:
                res.append(combination.copy())
                return
            if sum > target:
                return

            # We want the value at i
            combination.append(candidates[i])
            dfs(i, sum + candidates[i])

            # We don't want the value at i
            combination.pop()
            if i + 1 < len(candidates):
                dfs(i + 1, sum)

        dfs(0, 0)
        return res