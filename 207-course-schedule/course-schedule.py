class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # First, create the adjacency list for the directed graph
        adjList = [[] for _ in range(numCourses)] # Make sure don't reference same list
        for a, b in prerequisites:
            adjList[b].append(a)
        
        # Cycle detection using 3 states
        # If dfs onto a course that is VISITING, then there is a cycle
        NOT_VISITED, VISITING, VISITED = 0, 1, 2
        state = [NOT_VISITED] * numCourses

        # Returns whether there is a cycle
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
            return False

        # Need to do a outer loop to make sure the whole graph is checked
        for course in range(numCourses):
            if state[course] == NOT_VISITED:
                if dfs(course):
                    return False
        return True