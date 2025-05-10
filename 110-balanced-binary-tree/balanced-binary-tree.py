# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        heightBalanced = True
        
        # returns the height of this node where leaf has height 0
        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal heightBalanced
            if not node:
                return -1 

            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            if abs(leftHeight - rightHeight) > 1:
                heightBalanced = False
            return max(leftHeight, rightHeight) + 1

        dfs(root)

        return heightBalanced