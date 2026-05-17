class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adj_list[src].append(dst)
        path = []
        def dfs(node):
            while adj_list[node]:
                # Pop since can only visit the edge once
                # Pop the 'a' first before 'z' to finish the 'z' first
                dfs(adj_list[node].pop())
            path.append(node)
        dfs("JFK")
        return path[::-1] # Reverse since we should have prepended