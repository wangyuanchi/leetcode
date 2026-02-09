# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            values.append(node.val)
            dfs(node.right)

        dfs(root)

        def constructBST(values: List[int]) -> Optional[TreeNode]:
            if not values:
                return None
            
            middle = len(values) // 2

            root = TreeNode(values[middle])
            root.left = constructBST(values[:middle])
            root.right = constructBST(values[middle + 1:])

            return root

        return constructBST(values)
