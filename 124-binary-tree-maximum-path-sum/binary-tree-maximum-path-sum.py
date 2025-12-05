# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        The max path sum must pass through some root/sub-root node.
        Hence, we can calculate the max of max path sum through all nodes.
        """
        max_path_sum = root.val

        def dfs(node):
            nonlocal max_path_sum

            if not node:
                return 0

            # Do not have to take the path if it is negative
            left_max_path = max(dfs(node.left), 0)
            right_max_path = max(dfs(node.right), 0)

            max_path_sum = max(max_path_sum, node.val + left_max_path + right_max_path)

            return node.val + max(left_max_path, right_max_path)

        dfs(root)

        return max_path_sum