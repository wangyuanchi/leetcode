# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = []
        queue.append([root, 0])

        while len(queue) > 0:
            l = queue.pop(0)
            if l[0].left: queue.append([l[0].left, l[1] + 1])
            if l[0].right: queue.append([l[0].right, l[1] + 1])
            
            # Append based on level
            if (len(res) == l[1]):
                res.append([])
            
            res[l[1]].append(l[0].val)
        
        return res