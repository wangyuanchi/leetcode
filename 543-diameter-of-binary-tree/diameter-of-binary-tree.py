# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal diameter

            if not node:
                return 0
            
            depthLeft = dfs(node.left)
            depthRight = dfs(node.right)

            # calculate the longest path through this node
            longestPath = depthLeft + depthRight

            # compare to the global longest path
            diameter = max(diameter, longestPath)

            # return the depth of this tree
            return max(depthLeft, depthRight) + 1 

        dfs(root)

        return diameter