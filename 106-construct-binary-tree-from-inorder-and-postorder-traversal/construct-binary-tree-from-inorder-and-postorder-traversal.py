# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        v_to_i = {}
        for i, v in enumerate(inorder):
            v_to_i[v] = i

        root_index = len(postorder) - 1
        def buildSubtree(l, r):
            nonlocal root_index

            if l > r:
                return None

            root_val = postorder[root_index]
            root = TreeNode(root_val)
            root_index -= 1

            mid = v_to_i[root_val]
            root.right = buildSubtree(mid + 1, r)
            root.left = buildSubtree(l, mid - 1)

            return root
        return buildSubtree(0, len(inorder) - 1)
