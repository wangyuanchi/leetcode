class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        combination = [] # Builder

        # For dealing with duplicates
        candidates = sorted(candidates)

        def dfs(i, sum):
            # Base case: Reached leaf
            if i == len(candidates):
                # Check for duplicate
                if sum == target:
                    res.append(combination.copy())
                return

            # The value at i is in the combination
            combination.append(candidates[i])

            # Early pruning prevent exploring subtree with impossible combinations
            if sum + candidates[i] <= target:
                dfs(i + 1, sum + candidates[i])

            # The value at i is not in the combination
            combination.pop()
            for j in range(i + 1, len(candidates) + 1):
                # This is so that the base leaf can be reached
                if j == len(candidates):
                    dfs(j, sum)
                    break

                if candidates[j] == candidates[i]:
                    continue
                else:
                    dfs(j, sum)
                    break

        dfs(0, 0)
        return res