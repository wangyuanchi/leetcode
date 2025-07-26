class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create the adjacency list
        adjList = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            adjList[prereq[1]].append(prereq[0])

        # Directed graph, cycle detection with topological ordering
        NOT_VISITED, VISITING, VISITED = 0, 1, 2
        state = [NOT_VISITED for _ in range(numCourses)]
        tpOrder = []
        
        # Returns whether there is a cycle or not
        def dfs(course):
            if state[course] == VISITED:
                return False

            if state[course] == VISITING:
                return True

            state[course] = VISITING

            for adjCourse in adjList[course]:
                if dfs(adjCourse):
                    return True

            state[course] = VISITED
            tpOrder.insert(0, course)

            return False

        for course in range(numCourses):
            if state[course] == NOT_VISITED:
                if dfs(course):
                    return []

        return tpOrder