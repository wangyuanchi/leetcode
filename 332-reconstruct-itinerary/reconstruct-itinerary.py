class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        Directed graph, Euler path, Hierholzer's Algorithm
        https://www.youtube.com/watch?v=8MpoO2zA2l4
        Key idea: Once DFS gets stuck at node with no unvisited outgoing edge,
        prepend this node to the result and backtrack.
        """

        tickets = sorted(tickets) # Since we need lexicographic order
        adj_list = {}

        # Construct the adjacency list
        for from_i, to_i in tickets:
            if from_i not in adj_list:
                adj_list[from_i] = [0, to_i]
            else:
                adj_list[from_i].append(to_i)
        
        # Keep track of count of remaining neighbours not visited
        for k, v in adj_list.items():
            adj_list[k][0] = len(adj_list[k]) - 1

        itinerary = []

        def dfs(node):
            if node not in adj_list or adj_list[node][0] == 0:
                itinerary.append(node)
                return

            while adj_list[node][0] != 0:
                next_neighbour_index = -adj_list[node][0]
                adj_list[node][0] -= 1 # Decrease first to prevent looping on cycle
                dfs(adj_list[node][next_neighbour_index])

            itinerary.append(node)

        dfs("JFK")

        return itinerary[::-1]