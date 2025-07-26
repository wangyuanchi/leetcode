class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Parent pointer with weighted union and path compression
        parent = [n for n in range(len(edges) + 1)]
        weight = [1 for n in range(len(edges) + 1)]

        def find(n1, n2):
            n1copy, n2copy = n1, n2
            # Get to the highest common ancestor
            while n1 != parent[n1]:
                n1 = parent[n1]
            while n2 != parent[n2]:
                n2 = parent[n2]
            
            # Path compression
            parent[n1copy] = n1
            parent[n2copy] = n2

            return n1 == n2            

        def union(n1, n2):
            # Get to the highest common ancestor
            while n1 != parent[n1]:
                n1 = parent[n1]
            while n2 != parent[n2]:
                n2 = parent[n2]
            
            # Weighted union
            if weight[n1] < weight[n2]:
                parent[n1] = n2
                weight[n2] += weight[n1]
            else:
                parent[n2] = n1
                weight[n1] += weight[n2]

        for a, b in edges:
            if find(a, b):
                return [a, b]
            else:
                union(a, b)