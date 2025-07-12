"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {} # Value is the copied node

        # Return the deep copied value of the node
        def dfs(node):
            # Base case: Already visited
            if node.val in visited:
                return visited[node.val]

            visited[node.val] = Node(node.val)

            for neighbor in node.neighbors:
                copiedNeighbour = dfs(neighbor)
                visited[node.val].neighbors.append(copiedNeighbour)
            
            return visited[node.val]

        return dfs(node)