# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # create dictionary to map subtree roots in preorder
        # with its index in inorder to know the values
        # in the left and right subtrees
        val_to_index = {}
        counter = 0
        for val in inorder:
            val_to_index[val] = counter
            counter += 1
        
        # index to track the current root in the dfs block
        pre_index = 0

        # returns the root of the subtree defined by left and right,
        # which are indexes in inorder array
        def dfs(left, right):
            nonlocal pre_index

            # For the children of leaf nodes
            if (left > right):
                return None 

            root = TreeNode(preorder[pre_index])            
            root_index = val_to_index[preorder[pre_index]]
            pre_index += 1 # will be the root for the very next dfs() in call stack

            root.left = dfs(left, root_index - 1)
            root.right = dfs(root_index + 1, right)
            return root

        return dfs(0, len(inorder) - 1)