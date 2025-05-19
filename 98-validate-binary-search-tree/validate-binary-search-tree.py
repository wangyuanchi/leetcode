# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valid = True
        
        # need to define the range of values that
        # all nodes in subtree inclusive of current node must be within
        # [lowerBound, upperBound], i.e. inclusive
        def dfs(node, lowerBound, upperBound):
            nonlocal valid

            if not node:
                return

            if node.left:
                if node.left.val >= node.val or node.left.val < lowerBound:
                    valid = False

            if node.right:
                if node.right.val <= node.val or node.right.val > upperBound:
                    valid = False

            dfs(node.left, lowerBound, node.val - 1)
            dfs(node.right, node.val + 1, upperBound)

        dfs(root, float("-inf"), float("inf"))
        return valid