class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = {}
        for index, equation in enumerate(equations):
            var1, var2 = equation
            if var1 not in adjList:
                adjList[var1] = {}
            if var2 not in adjList:
                adjList[var2] = {}
            adjList[var1][var2] = 1 / values[index]
            adjList[var2][var1] = values[index]

        res = []

        for index, query in enumerate(queries):
            q1, q2 = query
            if q1 not in adjList or q2 not in adjList:
                res.append(-1.0)
                continue


            if q1 in adjList[q2]:
                res.append(adjList[q2][q1])
                continue
            
            source = (q2, 1) # node and multiplier
            q = deque()
            visited = set()
            q.append(source)
            visited.add(source)

            while len(q) > 0:
                node, multiplier = q.popleft()

                # check whether the answer is found
                if node == q1:
                    res.append(multiplier)
                    break

                for neighbour, val in adjList[node].items():
                    if neighbour in visited:
                        continue
                    
                    visited.add(neighbour)
                    q.append((neighbour, multiplier * val))

            if len(res) == index:
                res.append(-1.0)

        return res
