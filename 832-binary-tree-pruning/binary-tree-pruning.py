# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # returns whether there contains a 1 or not
        def dfs(node):
            if not node:
                return False

            left_contains_one = dfs(node.left)
            right_contains_one = dfs(node.right)
            if not left_contains_one:
                node.left = None
            if not right_contains_one:
                node.right = None

            if not left_contains_one and not right_contains_one:
                return node.val == 1
            else:
                return True

        if not dfs(root):
            return None
        return root
