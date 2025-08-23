class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Edge case
        if len(points) == 1:
            return 0

        # Helper function for manhatten distance
        def md(u, v):
            return abs(u[0] - v[0]) + abs(u[1] - v[1])

        # Convert points to a list of tuples for easier management
        temp = []
        for point in points:
            temp.append(tuple(point))
        points = temp

        # Run Prim's Algorithm
        visited = set()
        minCost = 0
        pq = [[0, points[0]]]
        heapq.heapify(pq)

        while len(pq) > 0:
            node = heapq.heappop(pq)
            cost, u = node[0], node[1]

            if u in visited:
                continue
            else:
                visited.add(u)
                minCost += cost
            
            for neighbour in points:
                heapq.heappush(pq, [md(u, neighbour), neighbour])

        return minCost