class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the adjacency list
        # Key is curNode, val is list of (target, weight)
        adjList = {}
        for edge in times:
            if edge[0] in adjList:
                adjList[edge[0]].append((edge[1], edge[2]))
            else:
                adjList[edge[0]] = [(edge[1], edge[2])]
        
        # Fill up the priority queue
        pq = [(0, k)] # (best current estimate, curNode)
        heapq.heapify(pq)
        visited = set() # If in visited set, then ignore if popped from pq
        res = [2**31 - 1 for _ in range(n)]

        # Start SSSP Dijkstra
        while len(pq) > 0:
            node = heapq.heappop(pq)
            bestCurDist, curNode = node[0], node[1]

            if curNode in visited:
                continue
            else:
                visited.add(curNode)
                res[curNode - 1] = bestCurDist

            if curNode in adjList:
                for target, weight in adjList[curNode]:
                    heapq.heappush(pq, (bestCurDist + weight, target)) # Relax

        return -1 if max(res) == 2**31 - 1 else max(res)