# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = [root]
        res = ""

        while len(q) > 0:
            node = q.pop(0)
            if node:
                res += str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res += "*"
            
            # Add delimiter because values can be more than 1 digit
            res += ","

        return res[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")

        if data[0] == "*":
            return None

        root = TreeNode(int(data[0]))
        q = [root]

        l, r = 1, 2

        while r < len(data):
            l_node, r_node = None, None
            if data[l] != "*":
                l_node = TreeNode(int(data[l]))
            if data[r] != "*":
                r_node = TreeNode(int(data[r]))
            
            sub_root = q.pop(0)
            sub_root.left, sub_root.right = l_node, r_node

            # Only add to queue if it is not None
            if l_node:
                q.append(l_node)
            if r_node:
                q.append(r_node)

            l += 2
            r += 2

        return root
