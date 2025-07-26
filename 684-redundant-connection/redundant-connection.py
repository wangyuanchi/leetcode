class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Parent pointer with weighted union and path compression
        parent = [n for n in range(len(edges) + 1)]
        weight = [1 for n in range(len(edges) + 1)]

        # Do path compressions (not actually "changing edges", just changing pointers)
        # Weights are unaffected
        def hca(n):
            if parent[n] != n:
                parent[n] = hca(parent[n])
            return parent[n]

        def find(n1, n2):
            return hca(n1) == hca(n2)            

        def union(n1, n2):
            n1, n2 = hca(n1), hca(n2)     
                   
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