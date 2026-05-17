class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        indegreeList = [0] * numCourses
        for u, v in prerequisites:
            adjList[v].append(u)
            indegreeList[u] += 1

        q = deque()
        completed_courses = 0

        for i, deg in enumerate(indegreeList):
            if deg == 0:
                q.append(i)

        while len(q) > 0:
            i = q.popleft()
            completed_courses += 1

            for neighbour in adjList[i]:
                indegreeList[neighbour] -= 1
                if indegreeList[neighbour] == 0:
                    q.append(neighbour)

        return completed_courses == numCourses
