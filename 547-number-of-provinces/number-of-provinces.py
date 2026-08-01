class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        provinces = 0

        def dfs(node):
            if visited[node]:
                return

            visited[node] = True

            for neighbour in range(len(isConnected[node])):
                if isConnected[node][neighbour]:
                    dfs(neighbour)

        for node in range(len(isConnected)):
            if not visited[node]:
                dfs(node)
                provinces += 1

        return provinces
