class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def get_next_values(value):
            if value == "0":
                return ["1", "9"]
            elif value == "9":
                return ["0", "8"]
            else:
                return [str(int(value) + 1), str(int(value) - 1)]
        
        def get_next_states(state):
            next_states = []
            for i, value in enumerate(state):
                next_state = [c for c in state]
                for next_value in get_next_values(value):
                    next_state[i] = next_value
                    next_states.append("".join(next_state))
            return next_states

        deadends = set(deadends)
        source = "0000"

        if source in deadends:
            return -1

        q = deque()
        visited = set()
        q.append((source, 0))
        visited.add(source)

        while len(q) > 0:
            node, steps = q.popleft()

            if node == target:
                return steps

            for neighbour in get_next_states(node):
                if neighbour in visited:
                    continue

                if neighbour in deadends:
                    continue
                
                visited.add(neighbour)
                q.append((neighbour, steps + 1))

        return -1
