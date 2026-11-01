class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]

        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        leaves = deque()
        for i in range(n):
            if len(adj_list[i]) == 1:
                leaves.append(i)

        remaining_nodes = n
        
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                
                neighbor = adj_list[leaf].pop()
                
                adj_list[neighbor].remove(leaf)
                
                if len(adj_list[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)
