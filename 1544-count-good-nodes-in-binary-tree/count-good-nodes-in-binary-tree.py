# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        
        def dfs(node, maxOnPath):
            nonlocal result 
            if maxOnPath <= node.val:
                result += 1

            if node.left:
                dfs(node.left, max(maxOnPath, node.left.val))
            if node.right:
                dfs(node.right, max(maxOnPath, node.right.val))

        dfs(root, root.val)

        return result